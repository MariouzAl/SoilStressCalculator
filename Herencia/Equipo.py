from Jugador import TipoJugador, Zaguero, Delantero

class Equipo:
    def __init__(self,nombreZaguero:str,nombreDelantero:str) -> None:
        self.zaguero = Zaguero(nombreZaguero)
        self.delantero = Delantero(nombreDelantero)
        

    def pegarleAlaBola(self ,quienLePega:TipoJugador ):
        if(self.delantero.tipoJugador == quienLePega ):
            self.delantero.pegarleALaBola()
        else:
            self.zaguero.pegarleALaBola()