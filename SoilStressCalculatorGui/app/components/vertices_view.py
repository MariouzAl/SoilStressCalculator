import random
from typing import Any
from PyQt6.QtWidgets import QGridLayout, QGroupBox, QPushButton, QTableWidget,QTableView
from PyQt6.QtCore import pyqtSignal
from soil_vertical_stress_increment.punto import Punto2D

from .coordinate_delegate import MascaradeEdicion
from models.vertices_table_model import VerticesTableModel

class VerticesView(QGroupBox):
    on_calcular_clicked: pyqtSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__("Vertices")
        layout = QGridLayout()
        self.tableWidget= self.config_table()
        layout.addWidget(self.tableWidget,0,0,2,2)
        eliminar_button = QPushButton(text="Eliminar")
        eliminar_button.clicked.connect(self.delete_selected_row)
        layout.addWidget(eliminar_button,2,0)
        agregar_button = QPushButton(text="Añadir")
        agregar_button.clicked.connect(self.add_row)
        layout.addWidget(agregar_button,2,1)
        calcular_button = QPushButton(text="Calcular")
        calcular_button.clicked.connect(self.calcular_button_click_handler)
        layout.addWidget(calcular_button,3,0,1,2)
        self.setLayout(layout)

    def config_table(self):
        self.model = VerticesTableModel([Punto2D(1,1),Punto2D(2,1),Punto2D(2,2),Punto2D(1,2)]);
        table = QTableView();
        table.setModel(self.model)
        table.setObjectName("tableWidget");
        delegate = MascaradeEdicion()
        table.setItemDelegate(delegate)
        return table;

    def add_row(self):
        print('Adding Item')
        self.model.add_data(Punto2D(0.0,0.0))
        
    def delete_selected_row(self): 
        print('removing Item')
        current_index =  self.tableWidget.currentIndex()
        self.model.remove_selected_row(current_index)

        
    def calcular_button_click_handler(self):
        print('Calcular Clicked')
        self.on_calcular_clicked.emit('Calcular Clicked')
     
    def get_values(self)-> list[Punto2D]:
        return self.model.get_values()      