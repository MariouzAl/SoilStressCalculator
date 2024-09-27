from math import pi,atan,sqrt
from collections.abc import Callable

from ..arista import AristaWrapper

def caclJi(a:float,c:float):
        return c/(sqrt((1)+(a**2)))

def calcNi(a:float,c:float):
        return ((a**2)*(c))/((1)+(a**2)+(c**2))

def FrolichX2Reducer(valorSobrecarga:float)->Callable[[float,AristaWrapper],float]:
    def reducerFunction(acc:float,arista:AristaWrapper)->float:
            J1i= caclJi(c=arista.C1,a=arista.a)
            J2i= caclJi(c=arista.C2,a=arista.a)
            Dszi =((valorSobrecarga)/(2*pi))*(((1)/(sqrt((1)+(arista.a**2))))*((atan(J2i))-(atan(J1i))))
            return acc+Dszi
    return reducerFunction

def FrolichX4Reducer(valorSobrecarga:float)->Callable[[float,AristaWrapper],float]:
    def reducerFunction(acc:float,arista:AristaWrapper)->float:
            J1= caclJi(c=arista.C1,a=arista.a)
            J2= caclJi(c=arista.C2,a=arista.a)
            N1= calcNi(a=arista.a,c=arista.C1)
            N2= calcNi(a=arista.a,c=arista.C2)
            Dszi =((valorSobrecarga)/(4*(pi)))*(((1)/((1)+(arista.a**2)))*((((((3)*(arista.a**2))+(2))/(sqrt((1)+(arista.a**2))))*((atan(J2))-(atan(J1))))+(N2)-(N1)))
            return acc+Dszi

    return reducerFunction