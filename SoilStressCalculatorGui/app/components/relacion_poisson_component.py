from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator


class RelacionPoissonComponent(QVBoxLayout):
    def __init__(self):
        super().__init__();

        self.label = QLabel('Relacion de poisson:')
        self.inputLine = QLineEdit()
        self.addWidget(self.label)
        self.addWidget(self.inputLine)
        rx = QRegularExpression("-?\\d+(\\.\\d+)?")
        validator = QRegularExpressionValidator(rx)
        self.inputLine.setValidator(validator)
        
        

    def hide(self):
        self.label.hide()
        self.inputLine.hide()
    def show(self):
        self.label.show()
        self.inputLine.show()

    def getValue(self)->float:
        try:
            return float(self.inputLine.text())
        except:
            return 0
    
    def setValue(self,value:float)->None:
        self.inputLine.setText(str(value))