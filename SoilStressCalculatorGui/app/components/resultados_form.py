from typing import Any
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)
from PyQt6.QtCore import pyqtSignal

from models.input_file_formats import InputFileFormat


class ResultadosForm(QVBoxLayout):
    SAVE_ALL = 1
    SAVE_CURRENT = 0
    on_save_as :pyqtSignal = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.incremento_esfuerzo_input = QLineEdit()
        self.incremento_esfuerzo_input.setReadOnly(True)
        self.addWidget(QLabel("Incremento Esfuerzo"))
        self.addWidget(self.incremento_esfuerzo_input)
        self.addWidget(QLabel("Exportar"))
        tabla_actual_button = QPushButton("TablaActual")
        tabla_actual_button.clicked.connect(self.on_export_clicked(tabla_actual_button,self.SAVE_CURRENT))
        self.addWidget(tabla_actual_button)
        todo_button = QPushButton("Todo")
        todo_button.clicked.connect(self.on_export_clicked(todo_button,self.SAVE_ALL))
        self.addWidget(todo_button)

    def on_export_clicked(self,parent:Any, type:int):
        def on_clicked_slot():
            file_filter = f"{InputFileFormat.EXCEL.value}"
            dialog = QFileDialog(parent, "Guardar archivo" if type==self.SAVE_CURRENT else "Guardar archivo multiple", ".", file_filter)
            dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            if dialog.exec():
                [fileNames] = dialog.selectedFiles()
                self.on_save_as.emit((fileNames,type))
        
        return on_clicked_slot
