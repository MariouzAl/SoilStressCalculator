from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QVBoxLayout


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