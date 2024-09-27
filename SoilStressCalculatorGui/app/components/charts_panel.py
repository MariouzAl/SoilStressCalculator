from PyQt6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout


class ChartsPanel(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"background-color:#226a5a21")
        layout= QVBoxLayout()
        layout.addWidget(QPushButton("Grafica"))
        self.setLayout(layout)