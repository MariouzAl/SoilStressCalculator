from dataclasses import dataclass

from soil_vertical_stress_increment.punto import Punto2D
from .vertices_view import VerticesView
from .punto_3d_form_widget import Punto3DFormWidget, Punto3DFormWidgetData


from PyQt6.QtWidgets import QVBoxLayout, QWidget;
from PyQt6.QtCore import pyqtSignal


        
@dataclass
class CalculateParams:
    punto_3d_data:Punto3DFormWidgetData;
    vertices_data:list[Punto2D];


class SidePanel(QWidget):
    on_calculate:pyqtSignal = pyqtSignal(CalculateParams)
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.punto_3d_widget = Punto3DFormWidget()
        layout.addWidget(self.punto_3d_widget)
        self.vertices_view = VerticesView()
        self.vertices_view.on_calcular_clicked.connect(self.on_calcular_clicked_slot)
        layout.addWidget(self.vertices_view)
        self.setLayout(layout)
        
    def on_calcular_clicked_slot(self,_):
        punto_3d_data=self.punto_3d_widget.getValues();
        vertices_data = self.vertices_view.get_values()
        self.on_calculate.emit(CalculateParams(punto_3d_data=punto_3d_data,vertices_data=vertices_data))
        
