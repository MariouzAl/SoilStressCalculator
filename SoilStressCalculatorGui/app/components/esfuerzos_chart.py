from  pyqtgraph import GraphicsLayoutWidget, PlotItem,PlotDataItem,InfiniteLine
from PyQt6.QtGui import QPen, QColor
from PyQt6.QtCore import Qt
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
