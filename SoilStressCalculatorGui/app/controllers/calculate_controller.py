from soil_vertical_stress_increment import SoilStressCalculator,Boussinesq,FrolichX2,FrolichX4

from models.methods_enum import MetodosCalculo
from components.side_panel import CalculateParams

class CalculateController:

    def calculate(self,params:CalculateParams):
        metodo_calculo:SoilStressCalculator= self.__get_calc_method(params)
        return metodo_calculo.calculate()

    def __get_calc_method(self, params:CalculateParams):
        if(params.punto_3d_data.rigidez==MetodosCalculo.BOUSSINESQ_X3.value):
            return Boussinesq(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
        elif(params.punto_3d_data.rigidez==MetodosCalculo.FROLICH_X2.value):
            return FrolichX2(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
        elif(params.punto_3d_data.rigidez==MetodosCalculo.FROLICH_X4.value):
            return FrolichX4(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
        else:
            print('No implementation for Westergaard')
            return Boussinesq(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
            