
from models.default_input_data import DEFAULT_INPUT_DATA
from components.CalculateParams import CalculateParams
from components.Punto3DFormWidgetData import Punto3DFormWidgetData
from models.input_file_formats import InputFileFormat
from models.methods_enum import MetodosCalculo
from components.relacion_poisson_component import RelacionPoissonComponent
from components.rigidez_view import RigidezView
from components.secciones_analisis_view import SeccionesAnalisisView
from components.get_InputWithLabel import InputWithLabel, getInputWithLabel;
from utils.get_InputFile_parser import getInputFileParser

from soil_vertical_stress_increment import Punto3D
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QToolBar,QFileDialog
from PyQt6.QtGui import QAction


class Punto3DFormWidget(QGroupBox):
    fileImported : pyqtSignal = pyqtSignal(CalculateParams)
    
    def __init__(self):
        super().__init__("Parametros iniciales")
        layout = QVBoxLayout()
        self.draw_toolbar(layout)
        layout.addWidget(QLabel("Valor de sobrecarga:"))
        self.q=getInputWithLabel(title='q',unit='t/m2')
        layout.addWidget(self.q)
        title_label=QLabel("Posicion del punto P:")
        layout.addWidget(title_label)
        self.add_form(layout=layout)
        self.setLayout(layout)
        self.fileImported.connect(self.file_imported_slot)

    def add_form(self,layout:QVBoxLayout):
        self.xp:InputWithLabel=getInputWithLabel(title='Xp')
        self.yp:InputWithLabel=getInputWithLabel(title='Yp')
        self.zp:InputWithLabel=getInputWithLabel(title='z ')
        self.poisonComponent = RelacionPoissonComponent()
        self.rigidez= RigidezView()
        self.rigidez.onChanged.connect(self.change_method)
        secciones_analisis = SeccionesAnalisisView()
        secciones_analisis.hide()
        layout.addWidget(self.xp)
        layout.addWidget(self.yp)
        layout.addWidget(self.zp)
        layout.addLayout(secciones_analisis)
        layout.addLayout(self.poisonComponent)
        layout.addLayout(self.rigidez)
    
    def getValues(self)->Punto3DFormWidgetData:
        x= self.xp.get_value()
        y= self.yp.get_value()
        z= self.zp.get_value()
        q= self.q.get_value()
        rigidez = self.rigidez.getValue()
        relacionPoisson =  self.poisonComponent.getValue()
        
        return Punto3DFormWidgetData(
            punto=Punto3D(x,y,z),
            q=q,
            rigidez=rigidez,
            relacionPoisson=relacionPoisson)
        
    def change_method(self,value:tuple):
        if(value==MetodosCalculo.WESTERGAARD.value):
            self.poisonComponent.show()
        else:
            self.poisonComponent.hide()
            
    def draw_toolbar(self, layout):
        toolbar = QToolBar("Barra de herramientas")
        toolbar.setFloatable(False)
        layout.addWidget(toolbar)

        # Crear acciones para la barra de herramientas
        accion_nuevo = QAction("Nuevo", self)
        accion_importar = QAction("Importar", self)
        accion_importar.triggered.connect(self.open_file_dialog)
        accion_nuevo.triggered.connect(self.new_input_data_slot)

        # Agregar acciones a la barra de herramientas
        toolbar.addAction(accion_nuevo)
        toolbar.addAction(accion_importar)     
    
    def setValue(self,value:Punto3DFormWidgetData):
        self.xp.set_value(value.punto.x)
        self.yp.set_value(value.punto.y)
        self.zp.set_value(value.punto.z)
        self.q.set_value(value.q)
        self.rigidez.setValue(value.rigidez)
        self.poisonComponent.setValue(value.relacionPoisson)
    
    def open_file_dialog(self):
        file_filter =f"{InputFileFormat.JSON.value};;{InputFileFormat.EXCEL.value}";
        try:
            file_path,file_type_filter=QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            ".",
            file_filter
            );
            parser = getInputFileParser(file_type_filter);
            content=parser.read(file_path);
            self.fileImported.emit(content)
        except Exception as e:
            print("Error Ocurred : ",e)
    
    def new_input_data_slot(self):  
        self.fileImported.emit(DEFAULT_INPUT_DATA)
    
    def file_imported_slot(self,content:CalculateParams):
        self.setValue(content.punto_3d_data)