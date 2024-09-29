from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QTableWidget

from .resultados_form import ResultadosForm




class PanelResultados(QGroupBox):
    def __init__(self):
        super().__init__("Panel Resultados")
        """ self.setStyleSheet(f"background-color:#256a2f21") """
        layout= QHBoxLayout()
        self.result_form = ResultadosForm()
        layout.addLayout(self.result_form,1)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        columnas = ['xi', 'yi','xf',"yf",'Li','Fi','ai', 'C1i','C2i','θ1i','θ2i', 'B1i','B2i','σzi']
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        self.tableWidget.setObjectName("tableWidget")
        layout.addWidget(self.tableWidget,4)

        self.setLayout(layout)
    
    def add_results(self, result):
        self.result_form.add_result(result)
    