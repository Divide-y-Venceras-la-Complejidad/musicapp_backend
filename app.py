from flask import  Flask, jsonify
from mysql_connection import getMusicFromDatabase, getMusicFromDatabaseById, getMusicRangeFromDatabase
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
 
@app.route('/musics/<int:begin>/<int:end>')
@cross_origin()
def limit_musics(begin, end):
    musics = getMusicRangeFromDatabase(begin, end)
    jsonMusics = []
    for music in musics:
        jsonMusics.append(music.toJson())
    return jsonify(jsonMusics)
 

@app.route('/musics/<int:music_id>/<string:filter_type>')
@cross_origin()
def get_music_by_id_and_filter(music_id, filter_type):
    relatedMusicsId = executeMusicAlgorithm(music_id, filter_type)
    if relatedMusicsId:
        relatedMusicsId = [id + 1 for id in relatedMusicsId]
        musics = getMusicFromDatabaseById(relatedMusicsId)
        musics.sort(key=lambda x: relatedMusicsId.index(x.id))
        jsonMusics = []
        for music in musics:
            jsonMusics.append(music.toJson())
        return jsonify(jsonMusics)
    else:
        return jsonify({'error': 'Music not found'})


if __name__ == '__main__':
    app.run(debug=True)



     


