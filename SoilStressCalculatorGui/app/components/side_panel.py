from .vertices_view import VerticesView
from .punto_3d_form_widget import Punto3DFormWidget


from PyQt6.QtWidgets import QVBoxLayout, QWidget


class SidePanel(QWidget):
    def __init__(self):
        super().__init__()
        """ self.setStyleSheet(f"background-color:#212e5f21;") """
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.punto_3d_widget = Punto3DFormWidget()
        layout.addWidget(self.punto_3d_widget)
        self.vertices_view = VerticesView()
        self.vertices_view.on_calcular_clicked.connect(self.on_calcular_clicked_slot)
        layout.addWidget(self.vertices_view)
        self.setLayout(layout)
        
    def on_calcular_clicked_slot(self,val):
        print(val)
        print(self.punto_3d_widget.getValues())
        