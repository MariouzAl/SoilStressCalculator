""" Main Module it all starts here """
import sys

from soil_vertical_stress_increment.models import VerticalStressIncrementResults
from models.result_value_object import ResultValueObject
from models.result_model import ResultsModel
from components.CalculateParams import CalculateParams
from controllers import CalculateController,Controller
from components.resultados_form import ResultadosForm
from components.panel_resultados import PanelResultados
from components.charts_panel import ChartsPanel
from components.side_panel  import SidePanel

from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout, QInputDialog





# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    results_model:ResultsModel =  ResultsModel()
    calc_controller = CalculateController()
    controller= Controller(results_model)

    def __init__(self):
        super().__init__()
        title="DISTRIBUCION DE ESFUERZO VERTICAL DENTRO DE LA MASA DE SUELO POR EFECTO DE UNA CARGA UNIFORMEMENTE DI"
        self.setWindowTitle(title.capitalize())
        layout = QGridLayout()
        self.side_panel = SidePanel()
        self.side_panel.on_calculate.connect(self.calculate)
        layout.addWidget(self.side_panel,0,0,12,2)
        self.chart_panel = ChartsPanel()
        layout.addWidget(self.chart_panel,0,3,8,9)
        self.panel_resultados = PanelResultados()
        self.panel_resultados.on_save_as.connect(self.on_export_as_slot)
        layout.addWidget(self.panel_resultados,8,3,4,9)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.panel_resultados.tab_bar.currentTabChanged.connect(self.on_result_changed)
        self.panel_resultados.tab_bar.on_deleted_tab.connect(self.on_deleted_tab_slot)
        self.panel_resultados.tab_bar.on_double_click.connect(self.show_rename_dialog)
        self.results_model.on_result_added.connect(self.on_result_model_changed_slot)
        self.results_model.on_selected_item_changed.connect(self.on_selected_item_changed_slot)
        self.results_model.on_renamed.connect(self.on_rename_slot)


    def calculate(self,data:CalculateParams):
        self.controller.calculate(data)

    def on_result_model_changed_slot(self,result:ResultValueObject):
        self.panel_resultados.add_results(result.tabla_resultados,result.title)
        
    def on_result_changed(self,data:tuple[int,VerticalStressIncrementResults]):
        index=data[0]
        self.results_model.setCurrentIndex(index)
    
    def on_deleted_tab_slot(self,index:int):
        self.results_model.removeResult(index)
    
    def show_rename_dialog(self,index:int):
        data=self.results_model.getResultAt(index);
        dialog = QInputDialog()
        dialog.resize(350,200)
        dialog.setWindowTitle("Cambiar titulo")
        dialog.setLabelText("Introduzca el nuevo titulo:")
        dialog.setTextValue(data.title)
        ok = dialog.exec()                                
        text = dialog.textValue()
        """ text, ok = dialog.getText(None,"Cambiar titulo","Introduzca el nuevo titulo:",text=data.title) """
        if ok:
            self.results_model.rename(index,text)
        else:
            print("NO CHANGES")
        
    def on_selected_item_changed_slot (self,result:ResultValueObject):
        self.chart_panel.set_data(result.tabla_resultados,result.tabla_esfuerzos)
        self.panel_resultados.draw_current_data(result.tabla_resultados)
    
    def on_rename_slot(self, renameItem:tuple[int,str]):
        self.panel_resultados.rename_result(renameItem)
        
    def on_export_as_slot(self, file:tuple[str,int]):
        path, operation = file
        if operation == ResultadosForm.SAVE_CURRENT:
            data_to_save = [self.results_model.getCurrentItem()]
        if operation == ResultadosForm.SAVE_ALL:
            data_to_save= self.results_model.results
        self.controller.export_data(data_to_save,path)

app = QApplication(sys.argv)
app.setStyle("fusion")

window = MainWindow()
window.showMaximized()
app.exec()
