self._by_artist.insert(song.artist, song)
        print(f"Inserido: {song.artist}")
        print(f"Buscando: {self._by_artist.search(song.artist)}")