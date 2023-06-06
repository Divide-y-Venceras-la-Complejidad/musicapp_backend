class Music:
    def __init__(self, id, track_name, genre, artist_name, topic, release_date):
        self.id = id
        self.track_name = track_name
        self.genre = genre
        self.artist_name = artist_name
        self.topic = topic
        self.release_date = release_date
    
    def toJson(self):
        return {
            "id": self.id,
            "track_name": self.track_name,
            "genre": self.genre,
            "artist_name": self.artist_name,
            "topic": self.topic,
            "release_date": self.release_date
        }
    
    def __str__(self):
        return f"Music(id={self.id}, track_name='{self.track_name}', genre='{self.genre}', artist_name='{self.artist_name}', topic='{self.topic}', release_date='{self.release_date}')"