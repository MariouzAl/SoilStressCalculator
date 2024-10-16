from soil_vertical_stress_increment import SoilStressCalculator,Boussinesq,FrolichX2,FrolichX4,Westergaard
from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults
from models.methods_enum import MetodosCalculo
from components.CalculateParams import CalculateParams

class CalculateController:

    def calculate(self,params:CalculateParams)->VerticalStressIncrementResults:
        inputData = params
        metodo_calculo:SoilStressCalculator= self.__get_calc_method(inputData)
        result = metodo_calculo.calculate()
        result.input_data=inputData;
        return result

    def __get_calc_method(self, params:CalculateParams):
        if(params.punto_3d_data.rigidez==MetodosCalculo.BOUSSINESQ_X3.value):
            return Boussinesq(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
        elif(params.punto_3d_data.rigidez==MetodosCalculo.FROLICH_X2.value):
            return FrolichX2(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
        elif(params.punto_3d_data.rigidez==MetodosCalculo.FROLICH_X4.value):
            return FrolichX4(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data)
        elif(params.punto_3d_data.rigidez==MetodosCalculo.WESTERGAARD.value):
            return Westergaard(q=params.punto_3d_data.q,P=params.punto_3d_data.punto,vertices=params.vertices_data, relacion_poisson=params.punto_3d_data.relacionPoisson)
        else:
            raise TypeError(f"Metodo {params.punto_3d_data.rigidez} no esta disponible")
            