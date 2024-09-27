import sys
from components.panel_resultados import PanelResultados
from components.charts_panel import ChartsPanel
from components.side_panel  import SidePanel

from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout





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

window = MainWindow()
window.showMaximized()
app.exec()