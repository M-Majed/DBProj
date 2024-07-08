from dbfunctions import *
from DBManagement import DBM

class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def show_tracks(dbm: DBM):
        if not dbm:
            return None
        result = dbm.db_execute_read_query(
            """
            SELECT title, artist, duration FROM tracks;
            """,
            None,
        )
        return result
    
    def list_datatypes(self, dbm: DBM):
        tracks = self.show_tracks(dbm)
        if tracks:
            for track in tracks:
                print("Title:", track[0])
                print("Artist:", track[1])
                print("Duration:", track[2])
        else:
            print("No tracks found.")
# Example usage:

