from PyQt6.QtWidgets import QGroupBox, QHBoxLayout
from soil_vertical_stress_increment.models.vertical_stress_increment_result import (
    VerticalStressIncrementResults,
)
from .superficie_punto_chart import SuperficiePuntoChart
from .esfuerzos_chart import EsfuerzosChartContainer


class ChartsPanel(QGroupBox):
    esfuerzos_chart: EsfuerzosChartContainer

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.esfuerzos_chart = EsfuerzosChartContainer()
        layout.addWidget(self.esfuerzos_chart, 1)
        self.superficie_punto_chart = SuperficiePuntoChart()
        layout.addWidget(self.superficie_punto_chart, 1)
        self.setLayout(layout)

    def set_data(
        self, result: VerticalStressIncrementResults, data: list[tuple[float, float]]
    ):
        data_x: list[float] = []
        data_y: list[float] = []
        for x, y in data:
            print(x, y)
            data_x.append(x)
            data_y.append(y)

        self.esfuerzos_chart.update_data(x=data_y, y=data_x)
        print("result.input_data.vertices_data", len(result.input_data.vertices_data))
        self.superficie_punto_chart.set_data(result)
