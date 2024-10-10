import copy
import numpy as np
from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults
from .calculate_controller import CalculateController
from components.side_panel import CalculateParams

class ChartController : 
    controller = CalculateController()

    
    def calc_chart_data(self,data:CalculateParams,steps:float):
        self.data=data
        inicio = 0; 
        fin =data.punto_3d_data.punto.z;
        interval= self.generar_intervalos(steps, fin)
        rango=np.arange(inicio,fin+interval,interval)
        values = list(map(self.__calculate_increment_for_range,rango))
        return values

    def generar_intervalos(self, steps, fin)->float:
        return fin/steps
        
        
        
    def __calculate_increment_for_range(self,value:float)->tuple[float,float]:
        params = copy.deepcopy(self.data);
        params.punto_3d_data.punto.z=value
        return (-value,self.controller.calculate(params=params).get_total_result())
        