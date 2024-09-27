from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QShowEvent 
from PyQt6.QtWidgets import QComboBox, QLabel, QVBoxLayout
from models.methods_enum import MetodosCalculo

class RigidezView(QVBoxLayout):
    onChanged: pyqtSignal= pyqtSignal(tuple)
    __value:tuple
    def __init__(self):
        super().__init__()
        self.addWidget(QLabel('Rigidez'))
        self.cb =QComboBox()
        for item in MetodosCalculo:
            self.cb.addItem(item.value[0],item.value)
        self.cb.currentIndexChanged.connect(self.on_index_changed)
        self.addWidget(self.cb)
        self.cb.showEvent=self.child_event_handler
        
    def on_index_changed(self,index):
        item=self.cb.itemData(index)
        self.__value=item
        self.onChanged.emit(item)
        
    def child_event_handler(self,event:QShowEvent ):
        print("show event")
        print(event.isAccepted())
        self.on_index_changed(0)
    
    def getValue(self)->tuple:
        return self.__value
        