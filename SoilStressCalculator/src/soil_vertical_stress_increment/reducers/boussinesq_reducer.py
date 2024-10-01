from collections.abc import Callable
from math import atan, pi, sqrt

from ..models.vertical_stress_increment_result import BoussinesqIterationResult, VerticalStressIncrementResults

from ..arista import AristaWrapper

def BoussinesqReducer(valorSobrecarga:float)->Callable[[VerticalStressIncrementResults,AristaWrapper],VerticalStressIncrementResults]:
    def reducerFunction(acc:VerticalStressIncrementResults,arista:AristaWrapper)->VerticalStressIncrementResults:
            q1i=atan(arista.C1)
            q2i=atan(arista.C2)
            B1i=caclB(arista.a,arista.C1)
            B2i=caclB(arista.a,arista.C2)
            Dszi =((valorSobrecarga)/((2)*(pi)))*((q2i)-(q1i)-(atan(B2i))+(atan(B1i))+((B2i-B1i)/((arista.a**2)+1)))
            acc.push_result(BoussinesqIterationResult(arista=arista,q1i=q1i,q2i=q2i,B1i=B1i,B2i=B2i,Dszi=Dszi))
            return acc

    def caclB(a,c):
        return (a*c)/(sqrt((1)+(a**2)+(c**2)))
    return reducerFunction