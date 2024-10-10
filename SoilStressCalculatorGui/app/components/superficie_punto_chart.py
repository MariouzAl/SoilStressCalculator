import numpy as np

from  pyqtgraph.Transform3D  import Transform3D
from  pyqtgraph.opengl  import GLViewWidget,GLLinePlotItem, GLGridItem, GLScatterPlotItem,GLSurfacePlotItem;
from  pyqtgraph.opengl.items  import GLMeshItem

rojo=(255, 100, 100, 100)
verde= ( 100,255, 100, 100)
azul= ( 100, 100,255, 100)
morado = ( 1, .21,1, 100)
class SuperficiePuntoChart(GLViewWidget):
    def __init__(self):
        super().__init__()
        self.dibujar_cuadriculas()
        """ self.dibujar_superficie() """
        self.dibujar_punto()

    def dibujar_superficie(self):
        pass
        
    def dibujar_punto(self):
        sp3 = GLScatterPlotItem(pos=(0,0,-5), color=morado, size=1, pxMode=False)
        self.addItem(sp3)


        
    def dibujar_cuadriculas(self):
        ## create three grids, add each to the view
        xgrid = GLGridItem(color=rojo)
        ygrid = GLGridItem(color=verde)
        zgrid = GLGridItem(color=azul)
        self.addItem(xgrid)
        self.addItem(ygrid)
        self.addItem(zgrid)

        ## rotate x and y grids to face the correct direction
        xgrid.rotate(90, 0, 1, 0)
        ygrid.rotate(90, 1, 0, 0)
        
