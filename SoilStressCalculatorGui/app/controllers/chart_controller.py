import copy
import numpy as np
from .calculate_controller import CalculateController
from components.CalculateParams import CalculateParams

class ChartController : 
    controller = CalculateController()

    
    def calc_chart_data(self,data:CalculateParams,steps:float):
        self.data=data
        inicio = 0; 
        fin =data.punto_3d_data.punto.z;
        rango=np.linspace(inicio,fin,steps)
        values = list(map(self.__calculate_increment_for_range,rango))
        return values
        
        
    def __calculate_increment_for_range(self,value:float)->tuple[float,float]:
        params = copy.deepcopy(self.data);
        params.punto_3d_data.punto.z=value
        return (-value,self.controller.calculate(params=params).get_total_result())
        