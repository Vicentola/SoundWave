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
                funcao(data)







if __name__ == "__main__":
    p1 = PlayerManager()
    p2 = PlayerManager()
    print(p1 is p2)  # deve printar True
    p1.volume = 0.5
    print(p2.volume)  # deve printar 0.5 — são o mesmo objeto!
