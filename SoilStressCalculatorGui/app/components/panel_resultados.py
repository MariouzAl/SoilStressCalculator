from PyQt6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QVBoxLayout,
)
from soil_vertical_stress_increment.models.vertical_stress_increment_result import (
    BoussinesqIterationResult,
    FrolichX2IterationResult,
    FrolichX4IterationResult,
    IterationUnionResults,
    VerticalStressIncrementResults,
    WestergaardIterationResult,
)

from PyQt6.QtCore import pyqtSignal
from soil_vertical_stress_increment.models.methods_enum import MetodosCalculo
from services.datagrid_parser import StressIncrementResultsToDataGridParser
from components.results_tabbar import ResultsTabBar

from .resultados_form import ResultadosForm


class PanelResultados(QGroupBox):
    on_save_as: pyqtSignal = pyqtSignal(tuple)

    def __init__(self):
        super().__init__("Panel Resultados")
        outer_layout = QVBoxLayout()
        layout = QHBoxLayout()

        self.tab_bar = self.drawTabBar()
        #self.tab_bar.currentTabChanged.connect(self.on_resultado_selected_change_slot)
        outer_layout.addWidget(self.tab_bar, 1)

        self.result_form = ResultadosForm()
        self.result_form.on_save_as.connect(self.on_save_as_slot)
        layout.addLayout(self.result_form, 1)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        columnas = [
            "xi",
            "yi",
            "xf",
            "yf",
            "Li",
            "Fi",
            "ai",
            "C1i",
            "C2i",
            "θ1i",
            "θ2i",
            "B1i",
            "B2i",
            "σzi",
        ]
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        self.tableWidget.setObjectName("tableWidget")
        layout.addWidget(self.tableWidget, 4)

        outer_layout.addLayout(layout)
        self.setLayout(outer_layout)

    def drawTabBar(self):
        tab_bar = ResultsTabBar()
        return tab_bar

    def add_results(self, result: VerticalStressIncrementResults,label:str):
        self.tab_bar.addTab(result,label)
        self.tab_bar.setCurrentIndex(len(self.tab_bar.data) - 1)

    def _config_table_data(self, result: VerticalStressIncrementResults):
        iterations: list[IterationUnionResults] = result.get_iteration_results()
        datos = StressIncrementResultsToDataGridParser.getDataGrid(result.method, iterations)
        columnas = StressIncrementResultsToDataGridParser.getColumns(result.method)
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        self.tableWidget.clearContents()
        self.add_data_to_table(datos)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

    def add_data_to_table(self, datos):
        self.tableWidget.setRowCount(len(datos))
        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(valor)))

    def on_resultado_selected_change_slot(
        self, value: tuple[int, VerticalStressIncrementResults]
    ):
        print("on_resultado_selected_change_slot,", value)
        current_data:VerticalStressIncrementResults = value[1]
        self.draw_current_data(current_data)

    def draw_current_data(self, current_data:VerticalStressIncrementResults|None):
        if current_data is not None:
            self._config_table_data(current_data)
            self.result_form.incremento_esfuerzo_input.setText(
                str(current_data.get_total_result())
            )
        else:
            self.tableWidget.clear()
            self.result_form.incremento_esfuerzo_input.setText("")

    def on_save_as_slot(self, file: tuple[str, int]) -> None:
        self.on_save_as.emit(file)
    
    def rename_result(self,rename_item:tuple[int,str]):
        self.tab_bar.renameTab(rename_item)
