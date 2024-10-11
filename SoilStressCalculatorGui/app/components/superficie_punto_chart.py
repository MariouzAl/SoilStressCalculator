import numpy as np
from soil_vertical_stress_increment.models.vertical_stress_increment_result import VerticalStressIncrementResults
from utils import ear_clipping
from  pyqtgraph.opengl  import GLViewWidget,GLGridItem, GLScatterPlotItem,GLMeshItem
from soil_vertical_stress_increment.punto import Punto2D, Punto3D;

rojo=(255, 100, 100, 100)
verde= ( 100,255, 100, 100)
azul= ( 100, 100,255, 100)
morado = ( 1, .21,1, 100)
class SuperficiePuntoChart(GLViewWidget):
    def __init__(self):
        super().__init__()
        self.dibujar_cuadriculas()
        self.dibujar_superficies()
        self.dibujar_punto()

    def dibujar_superficies(self, vertices: list[Punto2D]=[Punto2D(1.0,1.0),Punto2D(2.0,1.0),Punto2D(2.0,2.0),Punto2D(1.0,2.0)],depth:float=0):
        depths=np.linspace(0,depth,50);
        for iteration_depth in  depths:
            face = self._draw_prism_upper_face(vertices,iteration_depth);
            self.addItem(face);

    def _draw_prism_upper_face(self, vertices,depth):
        verts =self.__get_vertex_list(vertices,depth);
        faces = list(map(self.__map_vertexez_to_indexes(verts),ear_clipping.triangulación_ear_clipping(verts)));
        verts= np.array(verts)
        m1 = GLMeshItem(vertexes=verts, faces=faces,  smooth=False, color=(1, 1, 0, 0.5) ,glOptions='translucent', drawEdges=True)
        return m1
        
    def dibujar_punto(self,P:Punto3D=Punto3D(1,1,5)):
        sp3 = GLScatterPlotItem(pos=(P.x,P.y,-P.z), color=(1, 0,0, 1), size=.5, pxMode=False )
        self.addItem(sp3)

    def __get_vertex_list(self,vertices :list[Punto2D],depth)-> list[list[float,float,float]]: 
        vertexes=[]
        for vertice in vertices:
           vertexes.append([vertice.x,vertice.y,depth])
        return vertexes
        
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
        
        
    def set_data(self,data:VerticalStressIncrementResults):
        print('vertices',len(data.input_data.vertices_data))
        print('vertices class variable',len(data.vertices))
        vertices=data.input_data.vertices_data
        print('vertices',len(vertices))
        P=data.P
        self.clear()
        self.dibujar_cuadriculas()
        self.dibujar_superficies(vertices,-P.z)
        self.dibujar_punto(P)
        
    def __map_vertexez_to_indexes(self,source_vertex:list[list[float,float,float]]):
        def  mapper(item:tuple[list[float,float,float],list[float,float,float],list[float,float,float]]):
            v1,v2,v3= item
            v1_index= source_vertex.index(v1)
            v2_index= source_vertex.index(v2)
            v3_index= source_vertex.index(v3)
            return [v1_index,v2_index,v3_index]
        return mapper

    def _crear_proyeccion(self, aristas:list[list[list[float]]] , depth):
        caras_prisma=list(map(lambda arista:[arista[0]+[0], arista[1]+[0],arista[0]+[depth], arista[1]+[depth]]  ,aristas))
        return caras_prisma