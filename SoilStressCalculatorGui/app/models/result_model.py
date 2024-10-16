from PyQt6 import QtCore;
from PyQt6.QtCore import pyqtSignal,QObject
from models.result_value_object import ResultValueObject

class ResultsModel(QObject):
    current_item:ResultValueObject;
    current_index:int;
    results : list[ResultValueObject]
    on_data_changed:pyqtSignal=pyqtSignal(list);
    on_result_added:pyqtSignal=pyqtSignal(ResultValueObject);
    on_selected_item_changed:pyqtSignal=pyqtSignal(ResultValueObject);
    
    def __init__(self):
        super().__init__();
        self.current_index=-1;
        self.results=[];
        
    
    def addResult(self,result:ResultValueObject):
        self.results.append(result);
        self.on_result_added.emit(result)
        self.on_data_changed.emit(self.results)
    
    def removeResult(self,index:int):
        value = self.results[index]
        self.results.remove(value);
        self.on_data_changed.emit(self.results)
        
    def clearData(self):
        self.results = []
        self.on_data_changed.emit(self.results)
        
    def setCurrentIndex(self, index:int):
        item = self.results[index]
        self.setCurrentItem(item)
        
    def setCurrentItem(self, item:ResultValueObject):
        self.index=self.results.index(item)
        self.current_item=self.results[self.index]
        self.on_selected_item_changed.emit(self.current_item)
    
    def getCurrentItem(self):
        return self.results[self.current_index]
        
    def getResultAt(self, index):
        return self.results[index]
    
    