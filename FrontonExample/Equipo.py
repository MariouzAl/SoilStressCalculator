from Jugador import Jugador, TipoJugador

class Equipo:
    def __init__(self,nombreZaguero:str,nombreDelantero:str) -> None:
        self.zaguero = Jugador(nombreZaguero,TipoJugador.ZAGUERO)
        self.delantero = Jugador(nombreDelantero,TipoJugador.DELANTERO)
        

    def pegarleAlaBola(self ,quienLePega:TipoJugador ):
        if(self.delantero.tipoJugador == quienLePega ):
            self.delantero.pegarleALaBola()
        else:
            self.zaguero.pegarleALaBola()