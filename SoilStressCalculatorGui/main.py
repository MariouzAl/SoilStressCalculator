import string
import sys
import numpy as np

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette,QColor
from PyQt6.QtWidgets import (QApplication,
                             QDoubleSpinBox,
                             QLabel,
                             QMainWindow,
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QWidget,
                             QGroupBox,
                             QGridLayout,
                             QComboBox,
                             QTableWidget,
                             QPushButton,
                             QLineEdit)




def getQDoubleSpinBox(title:string,unit:string='m')->QDoubleSpinBox:
        spin= QDoubleSpinBox()
        spin.setPrefix(f"{title}= ")
        spin.setSuffix(f" {unit}")
        spin.setRange(-np.inf,np.inf)
        return spin


class RigidezView(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(QLabel('Rigidez'))
        cb =QComboBox() 
        methods=[
            "χ=3 Boussinesq",
            "χ=2 Frolich",
            "χ=4 Frolich",
            "χ=1.5 WESTERGAARD(WIP)"
        ]
        cb.addItems(methods)
        self.addWidget(cb)
        

class SeccionesAnalisisView(QGridLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(QLabel('Secciones de analisis'),0,0,)
        x= getQDoubleSpinBox('x')
        self.addWidget(x,1,0)
        y= getQDoubleSpinBox('y')
        self.addWidget(y,1,1)
        z= getQDoubleSpinBox('z')
        self.addWidget(z)


class Punto3DFormWidget(QGroupBox):
    puntoValuesChanged:pyqtSignal
    def __init__(self):
        super().__init__("Parametros iniciales")

        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Valor de sobrecarga:"))
        q=getQDoubleSpinBox(title='q',unit='T/m2')
        layout.addWidget(q)
        title_label=QLabel("Posicion del punto P:")
        layout.addWidget(title_label)
        self.add_form(layout=layout)
        self.setLayout(layout)
        
    def add_form(self,layout:QVBoxLayout):
        xp=getQDoubleSpinBox(title='Xp')
        yp=getQDoubleSpinBox(title='Yp')
        zp=getQDoubleSpinBox(title='z')
        layout.addWidget(xp)
        layout.addWidget(yp)
        layout.addWidget(zp)
        layout.addLayout(SeccionesAnalisisView())
        layout.addLayout(RigidezView())
    
  
class VerticesView(QGroupBox):
    def __init__(self): 
        super().__init__("Vertices")
        layout = QGridLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.clicked.connect(self.add_row)
        self.tableWidget.setHorizontalHeaderLabels(['Punto', 'xi(m)','yi(m)'])
        self.tableWidget.setObjectName("tableWidget")
        layout.addWidget(self.tableWidget,0,0,2,2)
        layout.addWidget(QPushButton(text="Eliminar"),2,0)
        layout.addWidget(QPushButton(text="Añadir"),2,1)
        layout.addWidget(QPushButton(text="Calcular"),3,0,1,2)
        self.setLayout(layout)

    def add_row(self):
        print('clicked')
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)


class SidePanel(QWidget):
    def __init__(self):
        super().__init__()
        """ self.setStyleSheet(f"background-color:#212e5f21;") """
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(Punto3DFormWidget())
        layout.addWidget(VerticesView())
        self.setLayout(layout)

        
class ChartsPanel(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"background-color:#226a5a21")
        layout= QVBoxLayout()
        layout.addWidget(QPushButton("Grafica"))
        self.setLayout(layout)

class ResultadosForm(QVBoxLayout):
    def __init__(self):
        super().__init__()
        coordenadasCb=QComboBox()
        items=["[0 0 5]"]
        coordenadasCb.addItems(items)
        incremento_esfuerzo_input= QLineEdit()
        
        self.addWidget(QLabel('Coordenadas'))
        self.addWidget(coordenadasCb)
        self.addWidget(QLabel('Incremento Esfuerzo'))
        self.addWidget(incremento_esfuerzo_input)
        self.addWidget(QLabel('Exportar'))
        self.addWidget(QPushButton('TablaActual'))
        self.addWidget(QPushButton('Todo'))
        
class PanelResultados(QGroupBox):
    def __init__(self):
        super().__init__("Panel Resultados")
        """ self.setStyleSheet(f"background-color:#256a2f21") """
        layout= QHBoxLayout()
        layout.addLayout(ResultadosForm(),1)
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        columnas = ['xi', 'yi','xf',"yf",'Li','Fi','ai', 'C1i','C2i','θ1i','θ2i', 'B1i','B2i','σzi']
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        self.tableWidget.setObjectName("tableWidget")
        layout.addWidget(self.tableWidget,4)
        
        self.setLayout(layout)



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DISTRIBUCION DE ESFUERZO VERTICAL DENTRO DE LA MASA DE SUELO POR EFECTO DE UNA CARGA UNIFORMEMENTE DI".capitalize())
        layout = QGridLayout()
        layout.addWidget(SidePanel(),0,0,12,3)
        layout.addWidget(ChartsPanel(),0,3,8,9)
        layout.addWidget(PanelResultados(),8,3,4,9)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setStyle("Breeze")

""" palette = QPalette()

palette.setColor(QPalette.ColorRole.Window,0xF0F0F0)  # fondo claro
palette.setColor(QPalette.ColorRole.l, 0x000000)  # texto oscuro
palette.setColor(QPalette.ColorRole.Text, 0x000000)  # texto oscuro 
app.setPalette(palette)
"""
window = MainWindow()
window.showMaximized()
app.exec()