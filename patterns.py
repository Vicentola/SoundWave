import random




class PlayerManager :

    # Singleton — garante apenas uma instância do player
    # cls é a própria classe, como o self mas para a classe
    # _instance guarda o único objeto criado
    # Primeira chamada: cria o objeto e salva em _instance
    # Chamadas seguintes: retorna o mesmo objeto

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        
        return cls._instance

    
    def __init__(self):
        self.volume = 1.0
        self.is_playing = False



class EventBus :

    def __init__(self):
        self._listeners = {}

    
    def subscribe(self, event, callback):
        
        if event not in self._listeners:
            self._listeners[event] = []

        self._listeners[event].append(callback)
        

    def emit(self, event, data):
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(data)


class Command:

    def execute(self):
        pass


    def undo(self):
        pass


class VolumeCommand(Command):

    def __init__(self, player, volume):
        self.player = player
        self.volume = volume
        self.prev_volume = None

    def execute(self):
        self.prev_volume = self.player.volume
        self.player.volume = self.volume

    def undo(self):
        self.player.volume = self.prev_volume


class PlaybackStrategy:
    def get_next(self, queue):
        pass

class NormalStrategy(PlaybackStrategy):
# vai fazer a execução de fila normal
    def get_next(self, queue):
        if queue:
            return queue.pop(0)
        return None

class ShuffleStrategy(PlaybackStrategy):

    def get_next(self, queue):
        if queue:
            song = random.choice(queue)
            queue.remove(song)
            return song
        return None






if __name__ == "__main__":


    p1 = PlayerManager()
    p2 = PlayerManager()
    print(p1 is p2)  # deve printar True
    p1.volume = 0.5
    print(p2.volume)  # deve printar 0.5 — são o mesmo objeto!
    bus = EventBus()    
    bus.subscribe("play", lambda data: print(f"Tocando: {data}"))
    bus.subscribe("play", lambda data: print(f"Atualizando interface: {data}"))
    bus.emit("play", "Bohemian Rhapsody")
    bus.emit("stop", "nada") 
    player = PlayerManager()
    print(f"Volume inicial: {player.volume}")

    cmd = VolumeCommand(player, 0.3)
    cmd.execute()
    print(f"Volume após execute: {player.volume}")

    cmd.undo()
    print(f"Volume após undo: {player.volume}")
    queue = ["Bohemian Rhapsody", "Billie Jean", "Creep", "Superstition"]

    normal = NormalStrategy()
    print(normal.get_next(queue))  # sempre o primeiro

    shuffle = ShuffleStrategy()
    print(shuffle.get_next(queue))  # aleatório
    print(queue)  # deve ter 2 músicas — uma foi removida pelo normal, outra pelo shuffle