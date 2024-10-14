from soil_vertical_stress_increment import Punto3D


import copy
from dataclasses import asdict, dataclass


@dataclass
class Punto3DFormWidgetData:
    q:float
    punto:Punto3D
    relacionPoisson:float
    rigidez:tuple

    def __deepcopy__(self,memo):
        datos=asdict(self)
        return Punto3DFormWidgetData(
            q=datos['q'],
            punto=copy.deepcopy(datos['punto'], memo),
            relacionPoisson=datos['relacionPoisson'],
            rigidez=tuple(copy.deepcopy(list(datos['rigidez']),memo))
            )