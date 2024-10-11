from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults


class ResultadosForm(QVBoxLayout):
    on_cb_selected :pyqtSignal = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.coordenadasCb=QComboBox()
        self.coordenadasCb.currentIndexChanged.connect(self.coordenadas_cb_changed)
        self.addWidget(self.coordenadasCb)
        self.coordenadasCb.setVisible(True)
        self.incremento_esfuerzo_input= QLineEdit()
        self.incremento_esfuerzo_input.setReadOnly(True)
        """ self.addWidget(QLabel('Coordenadas')) """
        self.addWidget(QLabel('Incremento Esfuerzo'))
        self.addWidget(self.incremento_esfuerzo_input)
        self.addWidget(QLabel('Exportar'))
        self.addWidget(QPushButton('TablaActual'))
        self.addWidget(QPushButton('Todo'))
    
    def add_result(self, result:VerticalStressIncrementResults):
        self.coordenadasCb.addItem(f"P=[{result.P.x},{result.P.y}, {result.P.z}] q={result.q} {result.method.value[0]}",result)
        
        
    def coordenadas_cb_changed(self,current_index):
        print("coordenadas_cb_changed",current_index)
        current_data:VerticalStressIncrementResults = self.coordenadasCb.itemData(current_index)
        print("current data ",current_data.get_total_result())
        self.incremento_esfuerzo_input.setText(str(current_data.get_total_result()))
        self.on_cb_selected.emit((current_index,current_data))