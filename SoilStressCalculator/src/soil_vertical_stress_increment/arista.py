import math
from.punto import Punto2D


class Arista:
    puntoInicial:Punto2D
    puntoFinal:Punto2D
    _largo:float
    _F:float
    
    @property 
    def largo(self): 
        return self._largo    
   
    @property 
    def F(self): 
        return self._F    
    
    def  __init__(self,puntoInicial:Punto2D,puntoFinal:Punto2D) -> None:
        self.puntoInicial=puntoInicial
        self.puntoFinal=puntoFinal
        self._largo = self._calcLargo(puntoInicial,puntoFinal)
        self._F = self._calcF(puntoInicial,puntoFinal)
        
    def _calcLargo(self,puntoInicial:Punto2D,puntoFinal:Punto2D)->float:
        x=puntoFinal.x-puntoInicial.x
        y=puntoFinal.y-puntoInicial.y
        return math.sqrt(math.pow(x,2)+math.pow(y,2))
    
    def _calcF(self,puntoInicial:Punto2D,puntoFinal:Punto2D)->float:
        return (puntoInicial.x * puntoFinal.y) - (puntoFinal.x * puntoInicial.y)
        
 
class AristaWrapper(Arista):
    _a:float
    _C1:float
    _C2:float
    def  __init__(self,arista:Arista,Zp:float) -> None:
         super().__init__(arista.puntoInicial,arista.puntoFinal)

         self._a= 0 if(self._F==0) else self._calcA(F=self._F,Zp=Zp,L=self._largo,)
         self._C1= self._calcC1(P1=self.puntoInicial,P2=self.puntoFinal,f=self.F)
         self._C2= self._calcC2(P1=self.puntoInicial,P2=self.puntoFinal,f=self.F)
    
    def _calcA(self,L:float,F:float,Zp:float)->float :
        return abs((Zp *L)/F)
    
    def _calcC1(self,P1:Punto2D,P2:Punto2D,f:float)->float:
        try:
            return (((P1.x)*(P2.x-P1.x))+((P1.y)*(P2.y-P1.y)))/f
        except:
            return 0
     
    def _calcC2(self,P1:Punto2D,P2:Punto2D,f:float)->float:
        try:
            return (((P2.x)*(P2.x-P1.x))+((P2.y)*(P2.y-P1.y)))/f
        except:
            return 0
    
    @property
    def a(self)->float:
        return self._a
    
    @property
    def C1(self)->float:
        return self._C1
    
    @property
    def C2(self)->float:
        return self._C2
        
 
    
if(__name__=='__main__'):
    arista = Arista(Punto2D(2,1),Punto2D(2,2))
    aw=AristaWrapper(arista,5)
    print(aw.largo)
    print(aw.F)   
    print(aw._a)   
    print(aw._C1)   
    print(aw._C2)   
    
    