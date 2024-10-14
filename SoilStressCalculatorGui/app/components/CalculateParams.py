import copy

from dataclasses import dataclass

from components.Punto3DFormWidgetData import Punto3DFormWidgetData
from soil_vertical_stress_increment.punto import Punto2D


@dataclass
class CalculateParams:
    punto_3d_data:Punto3DFormWidgetData;
    vertices_data:list[Punto2D];

    def __deepcopy__(self,memo):
        return CalculateParams(
            copy.deepcopy(self.punto_3d_data, memo),
            [copy.deepcopy(vertex, memo) for vertex in self.vertices_data]
        )