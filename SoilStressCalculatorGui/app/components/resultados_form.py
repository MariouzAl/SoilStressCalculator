from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults


class ResultadosForm(QVBoxLayout):
    on_cb_selected :pyqtSignal = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.incremento_esfuerzo_input= QLineEdit()
        self.incremento_esfuerzo_input.setReadOnly(True)
        """ self.addWidget(QLabel('Coordenadas')) """
        self.addWidget(QLabel('Incremento Esfuerzo'))
        self.addWidget(self.incremento_esfuerzo_input)
        self.addWidget(QLabel('Exportar'))
        self.addWidget(QPushButton('TablaActual'))
        self.addWidget(QPushButton('Todo'))
    