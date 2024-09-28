
from PyQt6.QtCore import QAbstractTableModel,Qt,QModelIndex
from soil_vertical_stress_increment.punto import Punto2D

class VerticesTableModel(QAbstractTableModel):
    COLUMN_LABELS = ["Xi(m)","Yi(m)"];
    INDEX_OF_Y_COLUMN=1; 

    def __init__(self, data:list[Punto2D]):
        super(VerticesTableModel, self).__init__()
        self._data:list[Punto2D] = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row= index.row()
            column=index.column()
            value = self._data[row]
            value = value.x if column==0 else value.y
            return str(value)

    def rowCount(self, _):
        return len(self._data)

    def columnCount(self, _):
        return 2

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.COLUMN_LABELS[section])

            if orientation == Qt.Orientation.Vertical:
                return str(section+1)
    
    def flags(self, _):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable
    

    def add_data(self,data:Punto2D):
        self.beginInsertRows(QModelIndex(), self.rowCount(None), self.rowCount(None));
        self._data.append(data);
        self.endInsertRows();
        
    def remove_selected_row(self,index:QModelIndex):
        current_row = index.row();
        print(f"deleting row {current_row}" )
        if(current_row is not -1):
            self.beginRemoveRows(QModelIndex(),current_row,current_row)
            self._data.pop(current_row)
            self.endRemoveRows()
        
    def setData(self, indice:QModelIndex, valor, rol):
        rowIndex =indice.row()
        colIndex =indice.column()
        if rol == Qt.ItemDataRole.EditRole:
            if(colIndex==VerticesTableModel.INDEX_OF_Y_COLUMN):
                self._data[rowIndex].y = float(valor)
            else:
                 self._data[rowIndex].x = float(valor)
            self.dataChanged.emit(indice, indice)
            return True
        return False
