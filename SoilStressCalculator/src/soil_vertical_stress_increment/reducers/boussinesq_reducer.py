from collections.abc import Callable
from math import atan, pi, sqrt

from ..arista import AristaWrapper

def BoussinesqReducer(valorSobrecarga:float)->Callable[[float,AristaWrapper],float]:
    def reducerFunction(acc:float,arista:AristaWrapper)->float:
            q1i=atan(arista.C1)
            q2i=atan(arista.C2)
            B1i=caclB(arista.a,arista.C1)
            B2i=caclB(arista.a,arista.C2)
            Dszi =((valorSobrecarga)/((2)*(pi)))*((q2i)-(q1i)-(atan(B2i))+(atan(B1i))+((B2i-B1i)/((arista.a**2)+1)))
            return acc+Dszi

    def caclB(a,c):
        return (a*c)/(sqrt((1)+(a**2)+(c**2)))
    return reducerFunction