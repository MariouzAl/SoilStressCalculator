from dataclasses import dataclass
from functools import reduce

from .methods_enum import MetodosCalculo

from ..arista import AristaWrapper

@dataclass
class IterationResult:
    arista:AristaWrapper
    Dszi:float


@dataclass
class BoussinesqIterationResult(IterationResult): 
    q1i:float
    q2i:float
    B1i:float
    B2i:float
    
@dataclass
class FrolichX2IterationResult(IterationResult):
    J1i:float
    J2i:float

@dataclass
class FrolichX4IterationResult(FrolichX2IterationResult):
    N1i:float
    N2i:float
    
IterationUnionResults = BoussinesqIterationResult|FrolichX2IterationResult|FrolichX4IterationResult


class VerticalStressIncrementResults:
    method:MetodosCalculo
    _results : list[IterationUnionResults]=[]
    __total_dzs:float=0.0
    
    def __init__(self,metodo_calculo):
        self._results : list[IterationUnionResults]=[]
        self.__total_dzs:float=0.0
        self.method=metodo_calculo;
    
    def push_result(self, result:IterationUnionResults )->None:
        self._results.append(result)
        
    def set_results(self,results:list[IterationUnionResults])->None:
        self._results=results
        self.calc_total_result()
        
    def set_total_result(self,result:float)->None:
        self.__total_dzs = result;
    
    def get_total_result(self)->float:
        return self.__total_dzs;
    
    def calc_total_result(self)->None:
        self.__total_dzs = reduce(lambda acc,current_item: acc+current_item.Dszi,self._results,0)
    
    def get_iteration_results(self)->list[IterationUnionResults]:
        return self._results;
    
    def get_iteration_at(self,index:int)->IterationUnionResults:
        return self._results[index]