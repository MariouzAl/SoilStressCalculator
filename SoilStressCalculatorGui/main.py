import string
import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
import numpy as np


class Punto3DFormWidget(QWidget):
    puntoValuesChanged:pyqtSignal
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Valor de sobrecarga:"))
        q=self.getQDoubleSpinBox(title='q',unit='T/m2')
        layout.addWidget(q)
        title_label=QLabel("Posicion del punto P:")
        layout.addWidget(title_label)
        self.add_form(layout=layout)
        self.setLayout(layout)
        
    def add_form(self,layout):

        xp=self.getQDoubleSpinBox(title='Xp')
        yp=self.getQDoubleSpinBox(title='Yp')
        zp=self.getQDoubleSpinBox(title='z')
        layout.addWidget(xp)
        layout.addWidget(yp)
        layout.addWidget(zp)
    
    def getQDoubleSpinBox(self,title:string,unit:string='m')->QDoubleSpinBox:
        spin= QDoubleSpinBox()
        spin.setPrefix(f"{title}= ")
        spin.setSuffix(f" {unit}")
        spin.setRange(-np.inf,np.inf)
        return spin



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DISTRIBUCION DE ESFUERZO VERTICAL DENTRO DE LA MASA DE SUELO POR EFECTO DE UNA CARGA UNIFORMEMENTE DI".capitalize())

        layout = QVBoxLayout()
     
        layout.addWidget(Punto3DFormWidget())


        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()