from  PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTabBar
from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults

class ResultsTabBar(QTabBar):
    currentTabChanged:pyqtSignal= pyqtSignal(tuple)
    data:list[VerticalStressIncrementResults] =[]
    
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        print ("TABS currentIndex",self.currentIndex())
        self.tabCloseRequested.connect(self.handle_close_request_slot)
        self.currentChanged.connect(self.handle_current_changed_slot)
    
    def addTab(self , item:VerticalStressIncrementResults):
        label = f"P=[{item.P.x},{item.P.y}, {item.P.z}] q={item.q} {item.method.value[0]}"
        self.data.append(item)
        super().addTab(label)
    
    
    def handle_close_request_slot(self,index: int):
        self.removeTab(index)
        self.data.remove(self.data[index])
        
    def handle_current_changed_slot(self, index):
        self.currentTabChanged.emit((index,self.data[index]))