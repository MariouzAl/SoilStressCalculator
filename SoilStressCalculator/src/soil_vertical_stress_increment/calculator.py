from collections.abc import Callable

from .models.methods_enum import MetodosCalculo
from .models.vertical_stress_increment_result import VerticalStressIncrementResults
from .arista import AristaWrapper
from .poligono import Poligono
from .punto import Punto2D, Punto3D,CalculadoraPuntoPrimo
from .reducers import BoussinesqReducer ,FrolichX2Reducer,FrolichX4Reducer,WestergaardReducer

from functools import reduce

    
class SoilStressCalculator:
    NAME:str
    metodoCalculo:MetodosCalculo
    
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D], strategy:Callable[[float],Callable[[VerticalStressIncrementResults,AristaWrapper],VerticalStressIncrementResults]]  ) -> None:
        self.q =q
        self.P =P
        self.vertices =vertices
        self.poligono = Poligono(self.__calcVerticesPrimos(self.vertices,self.P),P.z)
        self.strategy=strategy

    def calculate(self) -> VerticalStressIncrementResults:
        aristas =self.poligono.aristas
        initial_value=VerticalStressIncrementResults(metodo_calculo=self.metodoCalculo,P=self.P,q=self.q,vertices=self.vertices);
        result:VerticalStressIncrementResults=reduce(self.strategy,aristas,initial_value)
        result.calc_total_result()
        return result
    
    def __calcVerticesPrimos(self,vertices:list[Punto2D],P:Punto2D) -> list[Punto2D] : 
         return list(map(lambda vertice : CalculadoraPuntoPrimo.crearPuntoPrimo(vertice,P)  ,vertices))


class Boussinesq(SoilStressCalculator):
    NAME='BOUSSINESQ (X=3)'
    metodoCalculo:MetodosCalculo = MetodosCalculo.BOUSSINESQ_X3
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D]  ) -> None:
        super().__init__(q,P,vertices,BoussinesqReducer(q))

class FrolichX2(SoilStressCalculator):
    NAME='FROLICH (X=2)'
    metodoCalculo:MetodosCalculo = MetodosCalculo.FROLICH_X2
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D]  ) -> None:
        super().__init__(q,P,vertices,FrolichX2Reducer(q))

class FrolichX4(SoilStressCalculator):
    NAME='FROLICH (X=4)'
    metodoCalculo:MetodosCalculo = MetodosCalculo.FROLICH_X4
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D]  ) -> None:
        super().__init__(q,P,vertices,FrolichX4Reducer(q))

class Westergaard(SoilStressCalculator):
    NAME='WESTERGAARD (X=1.5)';
    metodoCalculo:MetodosCalculo = MetodosCalculo.WESTERGAARD
    
    def __init__(self,q:float, P : Punto3D, vertices :list[Punto2D] ,relacion_poisson:float ) -> None:
        super().__init__(q,P,vertices,WestergaardReducer(q,relacion_poisson=relacion_poisson))