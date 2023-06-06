from flask import  Flask, jsonify
from mysql_connection import getMusicFromDatabase
from flask_cors import CORS, cross_origin

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
 
if __name__ == '__main__':
    app.run(debug=True)


