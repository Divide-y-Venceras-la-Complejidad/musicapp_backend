from flask import  Flask, jsonify, send_file, make_response
from flask_cors import CORS, cross_origin
from music_algorithm import executeMusicAlgorithm
from music_mapping import getMusicFromMapAPI, getMusicRangeFromMapAPI, getMusicFromMapByIdAPI
 

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')  # Use the Agg backend

from music_algorithm import bfs_first_height_max_heap
from generate_graph_image import draw_graph
import io




app = Flask(__name__)
CORS(app)

@app.route('/musics')
@cross_origin()
def musics():
    musics = getMusicFromMapAPI()
    jsonMusics = []
    for music in musics:
        jsonMusics.append(music.toJson())
    return jsonify(jsonMusics)
 
@app.route('/musics/<int:begin>/<int:end>')
@cross_origin()
def limit_musics(begin, end):
    musics = getMusicRangeFromMapAPI(begin, end)
    jsonMusics = []
    for music in musics:
        jsonMusics.append(music.toJson())
    return jsonify(jsonMusics)
 

@app.route('/musics/<int:music_id>/<string:filter_type>')
@cross_origin()
def get_music_by_id_and_filter(music_id, filter_type):
    relatedMusicsId = executeMusicAlgorithm(music_id, filter_type)
    if relatedMusicsId:
        musics = getMusicFromMapByIdAPI(relatedMusicsId)
        musics.sort(key=lambda x: relatedMusicsId.index(x.id))
        jsonMusics = []
        for music in musics:
            jsonMusics.append(music.toJson())
        return jsonify(jsonMusics)
    else:
        return jsonify({'error': 'Music not found'})

#get music by id
@app.route('/musics/<int:music_id>')
@cross_origin()
def get_music_by_id(music_id):
    music = getMusicFromMapByIdAPI([music_id])
    if music:
        return jsonify(music[0].toJson())
    else:
        return jsonify({'error': 'Music not found'})

@app.route('/generate_graph/<int:Nodo>/<string:fileName>')
def generate_graph(Nodo, fileName):
    # Obtener los parámetros de la solicitud
    nodo = Nodo
    archivo = "archives/" + fileName + ".txt"

    # Cargar la matriz desde el archivo
    G1 = np.loadtxt(archivo)

    # Obtener los nodos conectados
    connected_nodes = bfs_first_height_max_heap(G1, nodo)
    connected_nodes.insert(0, nodo)  # Insertar el nodo principal al inicio de la lista

    # Crear el grafo utilizando NetworkX
    graph = draw_graph(G1, connected_nodes, weighted=True)

     # Dibujar el grafo utilizando NetworkX y Matplotlib
    plt.clf()  # Clear the previous plot
    pos = nx.shell_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="gold", edge_color="orange")

    # Guardar el gráfico en un objeto BytesIO
    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format='png')
    image_buffer.seek(0)

    # Crear una respuesta de Flask con los datos de la imagen
    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')

    # Retornar la respuesta de la API con la imagen
    return response


if __name__ == '__main__':
    app.run(debug=True)

     


