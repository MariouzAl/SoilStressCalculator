import sys

from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults
from controllers import CalculateController,ChartController
from components.panel_resultados import PanelResultados
from components.charts_panel import ChartsPanel
from components.side_panel  import CalculateParams, SidePanel

from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout





# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    controller = CalculateController()
    chart_controller =ChartController()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DISTRIBUCION DE ESFUERZO VERTICAL DENTRO DE LA MASA DE SUELO POR EFECTO DE UNA CARGA UNIFORMEMENTE DI".capitalize())
        layout = QGridLayout()
        self.side_panel = SidePanel()
        self.side_panel.on_calculate.connect(self.calculate)
        layout.addWidget(self.side_panel,0,0,12,2)
        self.chart_panel = ChartsPanel()
        layout.addWidget(self.chart_panel,0,3,8,9)
        self.panel_resultados = PanelResultados()
        layout.addWidget(self.panel_resultados,8,3,4,9)
        widget = QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        self.panel_resultados.result_form.on_cb_selected.connect(self.on_result_changed)

    
    def calculate(self,data:CalculateParams):
        result = self.controller.calculate(data)
        self.panel_resultados.add_results(result)
     
    def on_result_changed(self,data:tuple[int,VerticalStressIncrementResults]):
        result=data[1]
        chart_data=self.chart_controller.calc_chart_data(result.input_data,10)
        print (chart_data)
        self.chart_panel.set_data(chart_data)
        

app = QApplication(sys.argv)
app.setStyle("Breeze")

window = MainWindow()
window.showMaximized()
app.exec()