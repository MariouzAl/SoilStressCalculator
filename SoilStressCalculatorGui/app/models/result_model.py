from PyQt6 import QtCore;
from PyQt6.QtCore import pyqtSignal,QObject
from models.result_value_object import ResultValueObject


class ResultsModel(QObject):
    current_item:ResultValueObject;
    current_index:int;
    results : list[ResultValueObject]
    on_data_changed:pyqtSignal=pyqtSignal(tuple);
    on_result_added:pyqtSignal=pyqtSignal(ResultValueObject);
    on_selected_item_changed:pyqtSignal=pyqtSignal(ResultValueObject);
    
    def __init__(self):
        super().__init__();
        self.current_index=-1;
        self.results=[];
        
    
    def addResult(self,result:ResultValueObject):
        self.results.append(result);
        self.on_result_added.emit(result)
        self.on_data_changed.emit((self.results,self.current_index))
    
    def removeResult(self,index:int):
        new_index = self._recalculate_index(index)
        value = self.results[index]
        self.results.remove(value);
        self.current_index=new_index            
        self.on_data_changed.emit((self.results,self.current_index))
      
    def _recalculate_index(self,delete_index:int):
        list_length_after_removal = len(self.results)-1;
        indice_seleccionado= self.current_index
        if indice_seleccionado >= list_length_after_removal:
            # Recalcular el índice seleccionado
            indice_seleccionado = list_length_after_removal - 1
        if indice_seleccionado > delete_index:
            indice_seleccionado-=1
        return indice_seleccionado
        
            
        
    def clearData(self):
        self.results = []
        self.current_index=-1;
        self.on_data_changed.emit((self.results,self.current_index))
        
    def setCurrentIndex(self, index:int):
        if index!= -1:
            item = self.results[index]
            self.setCurrentItem(item)
        else: 
            self.setCurrentItem(ResultValueObject(None,None))
        
    def setCurrentItem(self, item:ResultValueObject):
        try:
            self.index=self.results.index(item)
            self.current_item=self.results[self.index]
            self.on_selected_item_changed.emit(self.current_item)
        except :
            self.on_selected_item_changed.emit(item)
            
    
    def getCurrentItem(self):
        return self.results[self.current_index]
        
    def getResultAt(self, index):
        return self.results[index]
    
    