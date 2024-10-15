import json
import pandas as pd;
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
        except FileNotFoundError as e:
            print("Archivo no encontrado",e)
        except json.JSONDecodeError:
            print("Error de sintaxis JSON")
    
    def parseJSONToCalculateParams(archivo:dict)->CalculateParams:
        rigidez = MetodosCalculo[archivo["rigidez"]]
        P = Punto3D(archivo['P']["x"],archivo['P']["y"],archivo['P']["z"])
        relacion_poisson =archivo["poisson"]
        punto_3d_data = Punto3DFormWidgetData(archivo['q'],P,relacion_poisson,rigidez.value)
        vertices_array = list(map(lambda vertice: Punto2D(vertice[0],vertice[1]) ,archivo['vertices']))
        return CalculateParams(punto_3d_data,vertices_array)
    
    
class ExcelInputParserReader:
    @staticmethod
    def read(file_path:str)->CalculateParams:
        try:
            input_file=pd.read_excel(file_path,index_col=None, header=None)
            return ExcelInputParserReader.parseExcelSheetToCalculateParams(input_file)
        except Exception as e:
            print("Ha ocurrido un error",e)
        
    
    def parseExcelSheetToCalculateParams(archivo:pd.DataFrame)->CalculateParams:
        type_value =archivo.loc[0,1];
        q = archivo.loc[1,1];
        P =Punto3D(archivo.loc[3,1],archivo.loc[4,1],archivo.loc[5,1])
        relacion_poisson =archivo.loc[6,1]
        rigidez = MetodosCalculo[archivo.loc[7,1]]
        vertexes=[]
        for _ ,row in archivo.iloc[9:].iterrows():
            vertexes.append([row[0],row[1]])
        
        punto_3d_data = Punto3DFormWidgetData(q=q,punto=P,relacionPoisson=relacion_poisson,rigidez=rigidez.value)
        vertices_array = list(map(lambda vertice: Punto2D(vertice[0],vertice[1]) ,vertexes))
        return CalculateParams(punto_3d_data,vertices_array)