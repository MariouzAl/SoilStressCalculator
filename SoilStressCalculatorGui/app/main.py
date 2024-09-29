import sys
from controllers.calculate_controller import CalculateController
from components.panel_resultados import PanelResultados
from components.charts_panel import ChartsPanel
from components.side_panel  import CalculateParams, SidePanel

from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout





# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DISTRIBUCION DE ESFUERZO VERTICAL DENTRO DE LA MASA DE SUELO POR EFECTO DE UNA CARGA UNIFORMEMENTE DI".capitalize())
        layout = QGridLayout()
        self.side_panel = SidePanel()
        self.side_panel.on_calculate.connect(self.calculate)
        layout.addWidget(self.side_panel,0,0,12,3)
        layout.addWidget(ChartsPanel(),0,3,8,9)
        self.panel_resultados = PanelResultados()
        layout.addWidget(self.panel_resultados,8,3,4,9)
        widget = QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def calculate(self,data:CalculateParams):
        controller = CalculateController()
        result = controller.calculate(data)
        self.panel_resultados.add_results(result)
        

app = QApplication(sys.argv)
app.setStyle("Breeze")

window = MainWindow()
window.showMaximized()
app.exec()