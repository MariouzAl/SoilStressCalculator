from PyQt6.QtWidgets import QStyledItemDelegate, QLineEdit
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator


class MascaradeEdicion(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, opciones, indice):
        editor = super().createEditor(parent, opciones, indice)
        if isinstance(editor, QLineEdit):
            editor.setValidator(QRegularExpressionValidator(QRegularExpression("-?\\d+(\\.\\d+)?")))  # Máscara para números de 1 a 3 dígitos
        return editor