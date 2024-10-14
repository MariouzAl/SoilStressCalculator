import json

from soil_vertical_stress_increment.models.methods_enum import MetodosCalculo
from soil_vertical_stress_increment.models.vertical_stress_increment_result import Punto3DFormWidgetData
from soil_vertical_stress_increment.punto import Punto2D, Punto3D
from components.CalculateParams import CalculateParams



class InputParserReader :
    
    def read(filepath:str)->CalculateParams:
        print(filepath) 
    
    
class JSONInputParserReader:
    @staticmethod
    def read(filepath:str)->CalculateParams:
        try:
            with open(filepath, 'r') as archivo:
                datos = json.load(archivo)
            return JSONInputParserReader.parseJSONToCalculateParams(datos)
        except FileNotFoundError:
            print("Archivo no encontrado")
        except json.JSONDecodeError:
            print("Error de sintaxis JSON")
    
    def parseJSONToCalculateParams(archivo:dict)->CalculateParams:
        rigidez = MetodosCalculo[archivo["rigidez"]]
        P = Punto3D(archivo['P']["x"],archivo['P']["y"],archivo['P']["z"])
        relacion_poisson =archivo["poisson"]
        punto_3d_data = Punto3DFormWidgetData(archivo['q'],P,relacion_poisson,rigidez.value)
        vertices_array = list(map(lambda vertice: Punto2D(vertice[0],vertice[1]) ,archivo['vertices']))
        return CalculateParams(punto_3d_data,vertices_array)