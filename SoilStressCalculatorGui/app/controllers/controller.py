import copy
import numpy as np

from services.export_service import ExportService
from models.result_value_object import ResultValueObject
from models.result_model import ResultsModel
from .calculate_controller import CalculateController
from components.CalculateParams import CalculateParams

class Controller : 
    controller = CalculateController()
    export_service:ExportService = ExportService()
    model:ResultsModel
    
    def __init__(self,model:ResultsModel):
        self.model = model;    
    
    def calculate(self,data:CalculateParams,steps:float=10):
        table_result=self.controller.calculate(params=data)
        self.data=data
        inicio = 0; 
        fin =data.punto_3d_data.punto.z;
        rango=np.linspace(inicio,fin,steps)
        chart_values = list(map(self.__calculate_increment_for_range,rango))
        title= f"P=({table_result.P.x},{table_result.P.y}, {table_result.P.z}) q={table_result.q} {table_result.method.value[0]}"
        result_vo= ResultValueObject(table_result,chart_values,title)
        self.model.addResult(result_vo)
        
        
    def __calculate_increment_for_range(self,value:float)->tuple[float,float]:
        params = copy.deepcopy(self.data);
        params.punto_3d_data.punto.z=value
        return (-value,self.controller.calculate(params=params).get_total_result())
        
        
    def export_data(self,data:list[ResultValueObject],path:str):
        self.export_service.export(data,path);