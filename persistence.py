import json
import os

from models import Song

class PersistenceManager:
    def __init__(self,file_path):
        self.file_path = file_path
        
    def save(self, library):
        data = {
            "songs": [song.to_dict() for song in library._songs.values()],
            #cria uma lista de dicionarios a partir dos objetivos Song, 
            #usando o metodo to_dict para converter cada objeto em um dicionario
        }
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
    def load(self, library):
        if not os.path.exists(self.file_path):
            return
        
        with open(self.file_path, "r", encoding = "utf-8") as file: # abre o arquivo de leitura
            songs_data = json.load(file)
            
        for song_data in songs_data["songs"]:
            song = Song.from_dict(song_data)
            library.add_song(song)
            
            
if __name__ == "__main__":
  
    from library import MusicLibrary

    lib = MusicLibrary()
    s1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
    s2 = Song("Billie Jean", "Michael Jackson", "Thriller", 294.0, genre="Pop")
    lib.add_song(s1)
    lib.add_song(s2)

    pm = PersistenceManager("data.json")
    pm.save(lib)
    print("Salvo!")

    lib2 = MusicLibrary()
    pm.load(lib2)
    print(lib2._songs)
      
        
            
        