
import csv
from music import Music

def read_csv_file(filename):
    music_dict = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        
        next(reader)  # Salta la primera fila que contiene los encabezados
        
        for row in reader:
            id = int(row[0])
            track_name = row[1]
            genre = row[2]
            artist_name = row[3]
            topic = row[4]
            release_date = row[5]
            
            music_obj = Music(id, track_name, genre, artist_name, topic, release_date)
            music_dict[id] = music_obj
        
    return music_dict

def getMusicFromMap(music_data):
    musics = list(music_data.values())
    return musics

def getMusicRangeFromMap(music_data, begin, end):
    musics = list(music_data.values())
    music_range = musics[begin:end+1]
    return music_range

def getMusicFromMapById(music_data, ids):
    musics = [music_data[id] for id in ids if id in music_data]
    return musics

