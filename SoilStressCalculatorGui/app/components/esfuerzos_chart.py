from  pyqtgraph import GraphicsLayoutWidget, PlotItem,PlotDataItem,InfiniteLine
from PyQt6.QtGui import QPen, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTabWidget,QTableWidget,QTableWidgetItem,QHeaderView
 # data can be a list of values or a numpy array


class EsfuerzosChart(GraphicsLayoutWidget):
    curva:PlotDataItem
    def __init__(self) -> None:
        super().__init__()
        self.p1:PlotItem = self.addPlot(row=0, col=0)
        self.p1.showGrid(x=True, y=True)
        self.curva = self.p1.plot(pen=(255,0,200),symbol='o')
        self.vLine = InfiniteLine(angle=90, movable=False)
        self.hLine = InfiniteLine(angle=0, movable=False)
        self.p1.addItem(self.vLine, ignoreBounds=True)
        self.p1.addItem(self.hLine, ignoreBounds=True)
        self.p1.scene().sigMouseMoved.connect(self.mouseMoved)
        
    def mouseMoved(self, evt):
        pos = evt
        vb=self.p1.vb
        if self.p1.sceneBoundingRect().contains(pos):
            mousePoint = vb.mapSceneToView(pos)
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())


    def update_data(self, x:list[float],y:list[float]):
        self.curva.setData(x=x,y=y)
        
class EsfuerzosTable(QTableWidget):
    def __init__(self)->None:
        super().__init__()
        self.setRowCount(4)
        columnas=["z","esfuerzo"]
        self.setColumnCount(len(columnas))
        self.setHorizontalHeaderLabels(columnas)
        self.setObjectName("tableWidget")
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
    def update_data(self, x:list[float],y:list[float]):
        self.clearContents()
        self.setRowCount(len(x))
        for index, _ in enumerate(x):
            self.setItem(index, 1, QTableWidgetItem(str(x[index])))
            self.setItem(index, 0, QTableWidgetItem(str(y[index])))
        
        

class EsfuerzosChartContainer(QTabWidget):
    chart:EsfuerzosChart
    table:EsfuerzosTable
    def __init__(self) -> None:
        super().__init__()
        self.chart =EsfuerzosChart()
        self.table =EsfuerzosTable()
        self.addTab(self.chart,"Grafica Esfuerzos")
        self.addTab(self.table,"Tabla Datos")
        

    def update_data(self, x:list[float],y:list[float]):
        self.chart.update_data(x,y)
        self.table.update_data(x,y)

