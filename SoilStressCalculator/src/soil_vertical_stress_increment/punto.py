class Punto2D:
    x:float
    y:float
    def __init__(self, x: float,y: float) -> None:
        self.x=x
        self.y = y
        

class Punto3D(Punto2D):
    z: float
    
    def __init__(self, x: float, y: float,z:float) -> None:
        super().__init__(x, y)
        self.z = z
    
    
class CalculadoraPuntoPrimo:    
    @staticmethod    
    def crearPuntoPrimo(puntoOrigen:Punto2D,puntoP:Punto2D) -> Punto2D:
        xp= puntoOrigen.x-puntoP.x
        yp= puntoOrigen.y-puntoP.y
        return Punto2D(xp,yp)
    

   
if(__name__=='__main__'):
    puntoPrueba:Punto2D = CalculadoraPuntoPrimo.crearPuntoPrimo(Punto2D(1,1),Punto2D(3,0))
    print(puntoPrueba.x,puntoPrueba.y)