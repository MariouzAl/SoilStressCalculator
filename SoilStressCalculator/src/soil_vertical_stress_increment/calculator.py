from collections.abc import Callable
from .arista import AristaWrapper
from .poligono import Poligono
from .punto import Punto2D, Punto3D,CalculadoraPuntoPrimo
from .reducers import BoussinesqReducer ,FrolichX2Reducer,FrolichX4Reducer

from functools import reduce

    
class SoilStressCalculator:
    NAME:str
    
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D], strategy:Callable[[float],Callable[[float,AristaWrapper],float]]  ) -> None:
        self.q =q
        self.P =P
        self.vertices =vertices
        self.poligono = Poligono(self.__calcVerticesPrimos(self.vertices,self.P),P.z)
        self.strategy=strategy

    def calculate(self) -> float:
        aristas =self.poligono.aristas
        result=reduce(self.strategy,aristas,0)
        return result
    
    def __calcVerticesPrimos(self,vertices:list[Punto2D],P:Punto2D) -> list[Punto2D] : 
         return list(map(lambda vertice : CalculadoraPuntoPrimo.crearPuntoPrimo(vertice,P)  ,vertices))


class Boussinesq(SoilStressCalculator):
    NAME='BOUSSINESQ (X=3)'
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D]  ) -> None:
        super().__init__(q,P,vertices,BoussinesqReducer(q))

class FrolichX2(SoilStressCalculator):
    NAME='FROLICH (X=2)'
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D]  ) -> None:
        super().__init__(q,P,vertices,FrolichX2Reducer(q))

class FrolichX4(SoilStressCalculator):
    NAME='FROLICH (X=4)'
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D]  ) -> None:
        super().__init__(q,P,vertices,FrolichX4Reducer(q))

