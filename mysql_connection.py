import mysql.connector
from music import Music 

def getMusicFromDatabase():
    
    mydb = mysql.connector.connect(
        user="michael",
        password="1234",
        database="tfdatabase"
    )

    mycursor = mydb.cursor()

    query = "SELECT * FROM music"
    mycursor.execute(query)
    allMusicData = mycursor.fetchall()

    musics = []

    for data in allMusicData:
        music_object = Music(*data)
        musics.append(music_object)
    
    return musics


def getMusicFromDatabase(id):
    mydb = mysql.connector.connect(
        user="michael",
        password="1234",
        database="tfdatabase"
    )

    mycursor = mydb.cursor()

    query = "SELECT * FROM music WHERE id = %s"
    params = (id,)
    mycursor.execute(query, params)
    musicData = mycursor.fetchone()

    if musicData:
        music_object = Music(*musicData)
        return music_object
    else:
        return None

def getMusicFromDatabaseList(ids):
    mydb = mysql.connector.connect(
        user="michael",
        password="1234",
        database="tfdatabase"
    )

    mycursor = mydb.cursor()

    # Prepare a parameterized query with placeholders for the IDs
    query = "SELECT * FROM music WHERE id IN ({})".format(','.join(['%s']*len(ids)))

    # Execute the query with the list of IDs as parameters
    mycursor.execute(query, ids)
    musicData = mycursor.fetchall()

    musics = []

    for data in musicData:
        music_object = Music(*data)
        musics.append(music_object)

    return musics

def getMusicFromDatabaseById(ids):
    mydb = mysql.connector.connect(
        user="michael",
        password="1234",
        database="tfdatabase"
    )

    mycursor = mydb.cursor()

    query = "SELECT * FROM music WHERE id IN (%s)"
    placeholders = ', '.join(['%s'] * len(ids))
    formatted_query = query % placeholders

    mycursor.execute(formatted_query, ids)
    allMusicData = mycursor.fetchall()

    musics = []

    for data in allMusicData:
        music_object = Music(*data)
        musics.append(music_object)

    return musics