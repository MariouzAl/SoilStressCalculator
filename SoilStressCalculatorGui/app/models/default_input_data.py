from soil_vertical_stress_increment.models.methods_enum import MetodosCalculo
from soil_vertical_stress_increment.punto import Punto2D, Punto3D
from components.Punto3DFormWidgetData import Punto3DFormWidgetData
from components.CalculateParams import CalculateParams



punto_3d_data=Punto3DFormWidgetData(q=10,
                                    punto=Punto3D(0,0,5),
                                    relacionPoisson=0,
                                    rigidez=MetodosCalculo.BOUSSINESQ_X3.value
                                    )    
vertices = [ 
            Punto2D(1,1),
            Punto2D(2,1),
            Punto2D(2,2),
            Punto2D(1,2),
            Punto2D(1,1),
            ]

DEFAULT_INPUT_DATA= CalculateParams(punto_3d_data,vertices)