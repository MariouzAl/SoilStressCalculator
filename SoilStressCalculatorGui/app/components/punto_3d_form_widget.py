from dataclasses import dataclass
from models.methods_enum import MetodosCalculo
from components.rigidez_view import RigidezView
from components.secciones_analisis_view import SeccionesAnalisisView
from utils.get_QDoubleSpinBox import InputWithLabel, getInputWithLabel
from soil_vertical_stress_increment import Punto3D

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QLabel, QVBoxLayout,QLineEdit



class RelacionPoissonComponent(QVBoxLayout):
    def __init__(self):
        super().__init__();
        
        self.label = QLabel('Relacion de poisson:')
        self.inputLine = QLineEdit()
        self.addWidget(self.label)
        self.addWidget(self.inputLine)
    
    def hide(self):
        self.label.hide()
        self.inputLine.hide()
    def show(self):
        self.label.show()
        self.inputLine.show()
        
    def getValue(self)->float:
        try:
            return float(self.inputLine.text) 
        except:
            return 0
        
            


class Punto3DFormWidget(QGroupBox):
    puntoValuesChanged:pyqtSignal
    
    def __init__(self):
        super().__init__("Parametros iniciales")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Valor de sobrecarga:"))
        self.q=getInputWithLabel(title='q',unit='T/m2')
        layout.addWidget(self.q)
        title_label=QLabel("Posicion del punto P:")
        layout.addWidget(title_label)
        self.add_form(layout=layout)
        self.setLayout(layout)

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
    
    def getValues(self):
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
            
            

@dataclass
class Punto3DFormWidgetData:
    q:float
    punto:Punto3D
    relacionPoisson:float
    rigidez:tuple
    
    