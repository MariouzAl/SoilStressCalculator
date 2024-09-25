from enum import Enum

class TipoJugador(Enum):
    DELANTERO = 'delantero'
    ZAGUERO = 'zaguero'

class Jugador:
    def __init__(self,nombre:str,tipoJugador:TipoJugador) -> None:
        self.nombre = nombre
        self.tipoJugador = tipoJugador

    def pegarleALaBola(self):
        print(f"{self.nombre} le pega a la bola")



class Zaguero(Jugador):
    def __init__(self,nombre:str) -> None:
        super().__init__(nombre,TipoJugador.ZAGUERO)
        
class Delantero(Jugador):
    def __init__(self,nombre:str) -> None:
        super().__init__(nombre,TipoJugador.DELANTERO)
        
        
