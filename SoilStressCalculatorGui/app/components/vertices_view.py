from typing import Any
from PyQt6.QtWidgets import QGridLayout, QGroupBox, QPushButton, QTableWidget
from PyQt6.QtCore import pyqtSignal

class VerticesView(QGroupBox):
    on_calcular_clicked: pyqtSignal = pyqtSignal(str)
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
        calcular_button = QPushButton(text="Calcular")
        calcular_button.clicked.connect(self.calcular_button_click_handler)
        layout.addWidget(calcular_button,3,0,1,2)
        self.setLayout(layout)

    def add_row(self):
        print('clicked')
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
        
    def calcular_button_click_handler(self):
        print('Calcular Clicked')
        self.on_calcular_clicked.emit('Calcular Clicked')
        