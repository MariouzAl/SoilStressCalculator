import math
import unittest

from src.soil_vertical_stress_increment import Boussinesq, FrolichX2, FrolichX4,Punto2D,Punto3D


class SoilStressCalculatorTestSuite(unittest.TestCase):
    
    valorSobrecarga = 10
    verticesCuadrado= [
            Punto2D(1,1),
            Punto2D(2,1),
            Punto2D(2,2),
            Punto2D(1,2),
        ];
    P=Punto3D(0,0,5);
    
    def test_Boussinesq_Calc(self):
        bstrategy= Boussinesq(self.valorSobrecarga,self.P,self.verticesCuadrado)
        result=bstrategy.calculate()
        self.assertNearlyEqual(a=result, b=0.12543662090840 )
    
    def test_FrolichX2_Calc(self):
        bstrategy= FrolichX2(self.valorSobrecarga,self.P,self.verticesCuadrado)
        result=bstrategy.calculate()
        self.assertNearlyEqual(a=result, b=0.0908822694186605 )
    
    def test_FrolichX4_Calc(self):
        bstrategy= FrolichX4(self.valorSobrecarga,self.P,self.verticesCuadrado)
        result=bstrategy.calculate()
        self.assertNearlyEqual(a=result, b=0.153957455838053 )

    def assertNearlyEqual(self,a,b,fraction=0.00000000000001,msg=None):
        if not math.isclose(a,b,rel_tol=fraction):
            if msg is None:
                self.fail("The given numbers %s and %s are not near each other."%(a,b))
            else:
                self.fail(msg)

if __name__ == '__main__':
    unittest.main()