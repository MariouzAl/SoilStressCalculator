from arista import Arista, AristaWrapper
from punto import Punto2D


class Poligono:
    __aristas : list[Arista]=[]
    __Zp=float
    
    def __init__(self,vertices:list[Punto2D],Zp=0) -> None:
        self.__Zp=Zp
        self.__aristas = self._calcAristas(vertices)
    
    def _calcAristas(self,vertices:list[Punto2D])->list[Arista]:
        aristas= []
        verticesLen= len(vertices)
        for i in range(0,verticesLen):
            if(i==verticesLen-1):
                arista = Arista(vertices[i],vertices[0])
                aristas.append(AristaWrapper(arista,self.__Zp))
                break
            arista =Arista(vertices[i],vertices[i+1])
            aristas.append(AristaWrapper(arista,self.__Zp))
        return aristas
    
    
    @property
    def aristas(self)->list[Arista]:
        return self.__aristas
    
    def getCantidadAristas(self) ->int:
        return len(self.__aristas)
    
    
if(__name__=='__main__'):
    verticesCuadrado= [
        Punto2D(1,1),
        Punto2D(2,1),
        Punto2D(2,2),
        Punto2D(1,2),
    ]
    cuadrado = Poligono(verticesCuadrado)
    print(cuadrado.getCantidadAristas())
    for arista in cuadrado.aristas:
        print(f'({arista.puntoInicial.x},{arista.puntoInicial.y})---({arista.puntoFinal.x},{arista.puntoFinal.y}) ')
        
