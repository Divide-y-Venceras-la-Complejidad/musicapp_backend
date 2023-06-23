
from methods import read_csv_file, getMusicFromMap, getMusicRangeFromMap, getMusicFromMapById

def getMusicFromMapAPI():
    music_data = read_csv_file('archives/datasettp2100datos.csv')
    musics = getMusicFromMap(music_data)
    return musics

def getMusicRangeFromMapAPI(begin, end):
    music_data = read_csv_file('archives/datasettp2100datos.csv')
    musics = getMusicRangeFromMap(music_data, begin, end)
    return musics

def getMusicFromMapByIdAPI(ids):
    music_data = read_csv_file('archives/datasettp2100datos.csv')
    musics = getMusicFromMapById(music_data, ids)
    return musics