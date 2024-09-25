from punto import Punto2D, Punto3D
from calculator import Boussinesq,FrolichX2,FrolichX4



if(__name__=='__main__'):        
    P= Punto3D(0,0,5)
    verticesCuadrado= [
            Punto2D(1,1),
            Punto2D(2,1),
            Punto2D(2,2),
            Punto2D(1,2),
        ]
    boussinesq_calc = Boussinesq(q=10,P=P,vertices=verticesCuadrado)
    f2_calc = FrolichX2(q=10,P=P,vertices=verticesCuadrado)
    f4_calc = FrolichX4(q=10,P=P,vertices=verticesCuadrado)
    print(f"{boussinesq_calc.NAME} {boussinesq_calc.calculate()}")
    print(f"{f2_calc.NAME} {f2_calc.calculate()}")
    print(f"{f4_calc.NAME} {f4_calc.calculate()}")
   