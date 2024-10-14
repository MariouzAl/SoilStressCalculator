from .CalculateParams import CalculateParams
from .vertices_view import VerticesView
from .punto_3d_form_widget import Punto3DFormWidget


from PyQt6.QtWidgets import QVBoxLayout, QWidget;
from PyQt6.QtCore import pyqtSignal;

        
class SidePanel(QWidget):
    on_calculate:pyqtSignal = pyqtSignal(CalculateParams)
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.punto_3d_widget = Punto3DFormWidget()
        self.punto_3d_widget.fileImported.connect(self.file_imported_slot)
        layout.addWidget(self.punto_3d_widget)
        self.vertices_view = VerticesView()
        self.vertices_view.on_calcular_clicked.connect(self.on_calcular_clicked_slot)
        layout.addWidget(self.vertices_view)
        self.setLayout(layout)       
        
    def on_calcular_clicked_slot(self,_):
        punto_3d_data=self.punto_3d_widget.getValues();
        vertices_data = self.vertices_view.get_values()
        self.on_calculate.emit(CalculateParams(punto_3d_data=punto_3d_data,vertices_data=vertices_data))
        
    def file_imported_slot(self,content:CalculateParams):
        self.vertices_view.set_values(content.vertices_data)