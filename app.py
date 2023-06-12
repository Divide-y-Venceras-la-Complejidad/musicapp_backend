from flask import  Flask, jsonify
from mysql_connection import getMusicFromDatabase, getMusicFromDatabaseById, getMusicFromDatabaseList
from flask_cors import CORS, cross_origin
from music_algorithm import executeMusicAlgorithm


app = Flask(__name__)
CORS(app)

@app.route('/musics')
@cross_origin()
def musics():
    musics = getMusicFromDatabase()
    jsonMusics = []
    for music in musics:
        jsonMusics.append(music.toJson())
    return jsonify(jsonMusics)
 
@app.route('/musics/<int:music_id>')
@cross_origin()
def get_music_by_id(music_id):
    relatedMusicsId = executeMusicAlgorithm(music_id)
    
    if relatedMusicsId:
        relatedMusicsId = [x + 1 for x in relatedMusicsId]
        musics = getMusicFromDatabaseList(relatedMusicsId)
        musics.sort(key=lambda x: relatedMusicsId.index(x.id))
         
        jsonMusics = []
        for music in musics:
            jsonMusics.append(music.toJson())
        return jsonify(jsonMusics)
    else:
        return jsonify({'error': 'Music not found'})

#create a method search music that receives the musicId and also a string called filterType

@app.route('/musics/<int:music_id>/<string:filter_type>')
@cross_origin()
def get_music_by_id_and_filter(music_id, filter_type):
    relatedMusicsId = executeMusicAlgorithm(music_id, filter_type)
    if relatedMusicsId:
        musics = getMusicFromDatabaseById(relatedMusicsId)
        jsonMusics = []
        for music in musics:
            jsonMusics.append(music.toJson())
        return jsonify(jsonMusics)
    else:
        return jsonify({'error': 'Music not found'})


if __name__ == '__main__':
    app.run(debug=True)



     


