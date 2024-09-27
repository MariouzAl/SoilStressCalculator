from utils.get_QDoubleSpinBox import getInputWithLabel


from PyQt6.QtWidgets import QGridLayout, QLabel


class SeccionesAnalisisView(QGridLayout):
    def __init__(self):
        super().__init__()
        self.add_items()

    def add_items(self):
        self.label = QLabel('Secciones de analisis')
        self.addWidget(self.label,0,0,)
        self.x= getInputWithLabel('x')
        self.addWidget(self.x,1,0)
        self.y= getInputWithLabel('y')
        self.addWidget(self.y,1,1)
        self.z= getInputWithLabel('z')
        self.addWidget(self.z)
      
    def hide(self):
        self.label.hide()
        self.x.hide()
        self.y.hide()
        self.z.hide()
        
    def show(self):
        self.label.show()
        self.x.show()
        self.y.show()
        self.z.show()