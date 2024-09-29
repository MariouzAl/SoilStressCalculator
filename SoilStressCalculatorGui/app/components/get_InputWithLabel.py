import numpy as np
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator


class InputWithLabel(QWidget):
        _value:float=0.0
        input:QLineEdit;
        def __init__(self,title:str,unit:str='m',value:float=0.0):
                super().__init__()
                self._createWidget(title,unit)
                self.set_value(value)
                
        def set_value(self, value:float):
                self._value= value;
                self.input.setText(str(value))
                print('set_value',self._value)
                
        def get_value(self)->float:
                return float(self.input.text())
        
        def _createWidget(self,title:str,unit:str='m')->QWidget:
                layout= QHBoxLayout()
                text_label = QLabel(f"{title}= ")
                unit_label = QLabel(f"{unit}")
                self.input= self._create_input()
                layout.addWidget(text_label)
                layout.addWidget(self.input,2)
                layout.addWidget(unit_label)
                self.setLayout(layout)
                self.setMaximumWidth(200)

        def _create_input(self):
            line_edit=QLineEdit()
            rx = QRegularExpression("-?\\d+(\\.\\d+)?")
            validator = QRegularExpressionValidator(rx)
            line_edit.setValidator(validator)
            line_edit.textEdited.connect(self.text_changed_slot)
            return line_edit
        
        def text_changed_slot(self,val):
                try:
                        self._value= float(val);
                except:
                        self._value= 0.0;
        
        def reset_values(self):
                self.set_value(0.0)
                


def getInputWithLabel(title:str,unit:str='m')->InputWithLabel:
        return InputWithLabel(title=title,unit=unit)