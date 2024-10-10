import numpy as np
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

        ## scale each grid differently
        """ xgrid.scale(0.2, 0.1, 0.1)
        ygrid.scale(0.2, 0.1, 0.1)
        zgrid.scale(0.1, 0.2, 0.1) """
        
        
        
        
"""
Simple examples demonstrating the use of GLMeshItem.
"""


import pyqtgraph as pg
import pyqtgraph.opengl as gl

app = pg.mkQApp("GLMeshItem Example")
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)

import numpy as np

## Example 1:
## Array of vertex positions and array of vertex indexes defining faces
## Colors are specified per-face

verts = np.array([
    [1,1, 0],
    [2,1, 0],
    [2, 2, 0],
    [1, 6, 0],
])
faces = np.array([
    [0, 1, 2,3,0],

])
colors = np.array([
    [1, 0, 0, 1],
    [0, 1, 0, 0.3],
    [0, 0, 1, 0.3],
    [1, 1, 0, 0.3]
])

## Mesh item will automatically compute face normals.
m1 = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors, smooth=False)
m1.translate(5, 5, 0)
m1.setGLOptions('additive')
w.addItem(m1)

""" 
## Example 2:
## Array of vertex positions, three per face
verts = np.empty((36, 3, 3), dtype=np.float32)
theta = np.linspace(0, 2*np.pi, 37)[:-1]
verts[:,0] = np.vstack([2*np.cos(theta), 2*np.sin(theta), [0]*36]).T
verts[:,1] = np.vstack([4*np.cos(theta+0.2), 4*np.sin(theta+0.2), [-1]*36]).T
verts[:,2] = np.vstack([4*np.cos(theta-0.2), 4*np.sin(theta-0.2), [1]*36]).T
    
## Colors are specified per-vertex
colors = np.random.random(size=(verts.shape[0], 3, 4))
m2 = gl.GLMeshItem(vertexes=verts, vertexColors=colors, smooth=False, shader='balloon', 
                   drawEdges=True, edgeColor=(1, 1, 0, 1))
m2.translate(-5, 5, 0)
w.addItem(m2)



## Example 3:
## sphere

md = gl.MeshData.sphere(rows=10, cols=20)
#colors = np.random.random(size=(md.faceCount(), 4))
#colors[:,3] = 0.3
#colors[100:] = 0.0
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m3 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')

m3.translate(5, -5, 0)
w.addItem(m3)


# Example 4:
# wireframe

md = gl.MeshData.sphere(rows=4, cols=8)
m4 = gl.GLMeshItem(meshdata=md, smooth=False, drawFaces=False, drawEdges=True, edgeColor=(1,1,1,1))
m4.translate(0,10,0)
w.addItem(m4)

# Example 5:
# cylinder
md = gl.MeshData.cylinder(rows=10, cols=20, radius=[1., 2.0], length=5.)
md2 = gl.MeshData.cylinder(rows=10, cols=20, radius=[2., 0.5], length=10.)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m5 = gl.GLMeshItem(meshdata=md, smooth=True, drawEdges=True, edgeColor=(1,0,0,1), shader='balloon')
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md2.setFaceColors(colors)
m6 = gl.GLMeshItem(meshdata=md2, smooth=True, drawEdges=False, shader='balloon')
m6.translate(0,0,7.5)

m6.rotate(0., 0, 1, 1)
#m5.translate(-3,3,0)
w.addItem(m5)
w.addItem(m6)
 """
if __name__ == '__main__':
    pg.exec()
     
""" 
## build a QApplication before building other widgets
import pyqtgraph as pg
pg.mkQApp()

## make a widget for displaying 3D objects
import pyqtgraph.opengl as gl
view = gl.GLViewWidget()
view.show()

## create three grids, add each to the view
xgrid = gl.GLGridItem()
ygrid = gl.GLGridItem()
zgrid = gl.GLGridItem()
view.addItem(xgrid)
view.addItem(ygrid)
view.addItem(zgrid)

## rotate x and y grids to face the correct direction
xgrid.rotate(90, 0, 1, 0)
ygrid.rotate(90, 1, 0, 0)

## scale each grid differently
xgrid.scale(0.2, 0.1, 0.1)
ygrid.scale(0.2, 0.1, 0.1)
zgrid.scale(0.1, 0.2, 0.1)
if __name__ == '__main__':
    pg.exec() """