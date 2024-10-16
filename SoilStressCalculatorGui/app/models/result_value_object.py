from soil_vertical_stress_increment.models.vertical_stress_increment_result import (
    VerticalStressIncrementResults,
)


class ResultValueObject:
    title: str

    def __init__(
        self,
        tabla_resultados: VerticalStressIncrementResults,
        tabla_esfuerzos: list[tuple[float, float]],
    ):
        self.tabla_resultados = tabla_resultados
        self.tabla_esfuerzos = tabla_esfuerzos
        self.title = f"P=({tabla_resultados.P.x},{tabla_resultados.P.y}, {tabla_resultados.P.z}) q={tabla_resultados.q} {tabla_resultados.method.value[0]}"
