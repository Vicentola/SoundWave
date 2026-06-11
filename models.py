

class Song:
    def __init__(self, title, artist, album, duration, genre="Desconhecido", play_count=0):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.genre = genre
        self.play_count = play_count

    def __repr__(self):
        return f"Song(title='{self.title}', artist='{self.artist}', album='{self.album}', duration={self.duration}, genre='{self.genre}', play_count={self.play_count})"
    
    def mark_as_played(self):
        self.play_count += 1
        
        
    @property
    def duration_str(self):
        
        """
    converte a duração de segundos para o formato mm:ss, 
    onde mm é minutos e ss é segundos. Por exemplo, 
    se a duração for 354 segundos, 
    a propriedade duration_str deve retornar "05:54".
    
    """
        
        mins, secs = divmod(int(self.duration), 60)
        return f"{mins:02d}:{secs:02d}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "duration": self.duration,
            "genre": self.genre,
            "play_count": self.play_count
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            artist=data["artist"],
            album=data["album"],
            duration=data["duration"],
            genre=data.get("genre", "Desconhecido"),
            play_count=data.get("play_count", 0)
            
        )
        
        """
        cls é a propria classe Song, é como chamar song mas dentro da classe
        
        metodo get com valores padrao para caso nao tenha a chave 
        no dicionario, evita erros de chave
        
        """
    
    
    


class Playlist:
    
    def __init__(self,name):
        self.name = name
        self.songs = []
        
    def add_song(self, song):
        self.songs.append(song)
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            
    def __repr__(self):
        return f"Playlist(name='{self.name}', songs={len(self.songs)})"



if __name__ == "__main__":
    s = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
    print(s)
    print(s.duration_str)
    s.mark_as_played()
    s.mark_as_played()
    print(s.play_count)    
    p = Playlist("My Favorites")
    p.add_song(s)
    print(p)
    print(p.songs)