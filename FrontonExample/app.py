from Equipo import Equipo;
from Jugador import TipoJugador;

equipo1=Equipo('Turi', 'Charro');
equipo2=Equipo('David', 'Carmelino');

equipo1.pegarleAlaBola(TipoJugador.DELANTERO)
equipo2.pegarleAlaBola(TipoJugador.ZAGUERO)
equipo1.pegarleAlaBola(TipoJugador.ZAGUERO)
equipo2.pegarleAlaBola(TipoJugador.DELANTERO)