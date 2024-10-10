
from collections.abc import Callable
from math import atan, pi, sqrt

from ..models.vertical_stress_increment_result import BoussinesqIterationResult, VerticalStressIncrementResults, WestergaardIterationResult

from ..arista import AristaWrapper

def WestergaardReducer(valorSobrecarga:float,relacion_poisson:float)->Callable[[VerticalStressIncrementResults,AristaWrapper],VerticalStressIncrementResults]:
    def reducerFunction(acc:VerticalStressIncrementResults,arista:AristaWrapper)->VerticalStressIncrementResults:
            k = calcK(relacion_poisson)
            q1i=atan(arista.C1)
            q2i=atan(arista.C2)
            W1=caclW(a=arista.a,c=arista.C1,k=k)
            W2=caclW(a=arista.a,c=arista.C2,k=k)
            Dszi =((valorSobrecarga)/((2)*(pi)))*((q2i)-(q1i)-(atan(W2))+(atan(W1)))
            acc.push_result(WestergaardIterationResult(arista=arista,q1i=q1i,q2i=q2i,W1i=W1,W2i=W2,Dszi=Dszi))
            return acc

    def calcK(n:float):
        return sqrt(((1)-(2*n))/((2)*(1-n)))
    
    def caclW(k,a,c):
        return (k*a*c)/(sqrt((1)+((k**2)*(a**2))+(c**2)))
    return reducerFunction