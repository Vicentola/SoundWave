from models import Song, Playlist
from structures import LinkedList, Hashtable, BinarySearchTree

class MusicLibrary:
    
    def __init__(self):
        
       self._songs = {}
       self._by_genre = Hashtable()
       self._by_artist = BinarySearchTree()
       self._playlists = {}
       
       
    def add_song(self,song):
        if song.title not in self._songs:
            self._songs[song.title] = song
            
        songs_by_genre = self._by_genre.get(song.genre)
        if songs_by_genre is None:
            self._by_genre.set(song.genre, [song])
            
        else:
            songs_by_genre.append(song) 
            self._by_genre.set(song.genre, songs_by_genre)
            
        self._by_artist.insert(song.artist, song)
        
          
    def get_songs_by_artist(self, artist):
        return self._by_artist.search(artist) or []
    
    def get_songs_by_genre(self, genre):
        return self._by_genre.get(genre) or []
    
    
    
    def search(self, query):
        results = []
    
        for song in self._songs.values():
            if query.lower() in song.title.lower() or query.lower() in song.artist.lower():
                results.append(song)
    
        return results
       
if __name__ == "__main__":
    
  
    

    lib = MusicLibrary()
    s1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
    s2 = Song("Creep", "Radiohead", "Pablo Honey", 238.0, genre="Rock")
    s3 = Song("Billie Jean", "Michael Jackson", "Thriller", 294.0, genre="Pop")
    lib.add_song(s1)
    lib.add_song(s2)
    lib.add_song(s3)
    print(lib._by_artist.search("Queen"))
    print(lib.get_songs_by_genre("Rock"))
    print(lib.get_songs_by_artist("Queen"))
    print(lib.search("billie"))