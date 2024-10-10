from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from soil_vertical_stress_increment.models.vertical_stress_increment_result import BoussinesqIterationResult, FrolichX2IterationResult, FrolichX4IterationResult, IterationUnionResults, VerticalStressIncrementResults

from soil_vertical_stress_increment.models.methods_enum import MetodosCalculo
from utils.get_columns import get_columns

from .resultados_form import ResultadosForm


def BousinessqColumnsMapper(val:BoussinesqIterationResult)->list[list[float]]:
       Xi=  val.arista.puntoInicial.x
       Yi=  val.arista.puntoInicial.y
       Xf=  val.arista.puntoFinal.x
       Yf=  val.arista.puntoFinal.y
       Li= val.arista.largo
       Fi= val.arista.F
       ai= val.arista.a
       C1i= val.arista.C1
       C2i= val.arista.C2
       q1i= val.q1i
       q12= val.q2i
       B1i= val.B1i
       B2i= val.B2i
       Dszi= val.Dszi
       return [Xi,
               Yi,
               Xf,
               Yf,
               Li,
               Fi,
               ai,
               C1i,
               C2i,
               q1i,
               q12,
               B1i,
               B2i,
               Dszi,]
       
def FrolichX2ColumnsMapper(val:FrolichX2IterationResult)->list[list[float]]:
    Xi=  val.arista.puntoInicial.x
    Yi=  val.arista.puntoInicial.y
    Xf=  val.arista.puntoFinal.x
    Yf=  val.arista.puntoFinal.y
    Li= val.arista.largo
    Fi= val.arista.F
    ai= val.arista.a
    C1i= val.arista.C1
    C2i= val.arista.C2
    J1i= val.J1i
    J2i= val.J2i
    Dszi= val.Dszi
    return [Xi,
            Yi,
            Xf,
            Yf,
            Li,
            Fi,
            ai,
            C1i,
            C2i,
            J1i,
            J2i,
            Dszi,]
    
def FrolichX4ColumnsMapper(val:FrolichX4IterationResult)->list[list[float]]:
    Xi=  val.arista.puntoInicial.x
    Yi=  val.arista.puntoInicial.y
    Xf=  val.arista.puntoFinal.x
    Yf=  val.arista.puntoFinal.y
    Li= val.arista.largo
    Fi= val.arista.F
    ai= val.arista.a
    C1i= val.arista.C1
    C2i= val.arista.C2
    J1i= val.J1i
    J2i= val.J2i
    N1= val.N1i
    N2= val.N2i
    Dszi= val.Dszi
    return [Xi,
            Yi,
            Xf,
            Yf,
            Li,
            Fi,
            ai,
            C1i,
            C2i,
            J1i,
            J2i,
            N1,
            N2,
            Dszi]; 
    
COLUMN_MAPPERS = {
    MetodosCalculo.BOUSSINESQ_X3: BousinessqColumnsMapper,
    MetodosCalculo.FROLICH_X2: FrolichX2ColumnsMapper,
    MetodosCalculo.FROLICH_X4: FrolichX4ColumnsMapper
    } 


class PanelResultados(QGroupBox):
    def __init__(self):
        super().__init__("Panel Resultados")
        layout= QHBoxLayout()
        self.result_form = ResultadosForm()
        layout.addLayout(self.result_form,1)
        self.result_form.on_cb_selected.connect(self.on_resultado_selected_change_slot)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        columnas = ['xi', 'yi','xf',"yf",'Li','Fi','ai', 'C1i','C2i','θ1i','θ2i', 'B1i','B2i','σzi']
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        self.tableWidget.setObjectName("tableWidget")
        layout.addWidget(self.tableWidget,4)

        self.setLayout(layout)
    
    def add_results(self, result:VerticalStressIncrementResults):
        self.result_form.add_result(result)

    
    def _config_table_data(self,result:VerticalStressIncrementResults):
        columnas=get_columns(result.method)
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        iterations:list[IterationUnionResults] = result.get_iteration_results()
        datos = self._get_data_matrix(result.method,iterations);
        self.tableWidget.clearContents()
        self.add_data_to_table(datos)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def add_data_to_table(self, datos):
        self.tableWidget.setRowCount(len(datos))
        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(valor)))

    def _get_data_matrix(self,methodo:MetodosCalculo,iterations:list[IterationUnionResults])->list[list[float]]:
        values=map(COLUMN_MAPPERS[methodo],iterations)
        return list(values)
        
    def on_resultado_selected_change_slot(self,value):
        print ("on_resultado_selected_change_slot,", value)
        self._config_table_data(value[1])
