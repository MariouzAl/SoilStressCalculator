from soil_vertical_stress_increment.models.methods_enum import MetodosCalculo
from soil_vertical_stress_increment.models.vertical_stress_increment_result import (
    BoussinesqIterationResult,
    FrolichX2IterationResult,
    FrolichX4IterationResult,
    IterationUnionResults,
    VerticalStressIncrementResults,
    WestergaardIterationResult,
)


BASE_COLUMNS = ("Xi'", "Yi'", "Xf'", "Yf'", "Li", "Fi", "ai", "C1i", "C2i")
BOUSSINESQ_COLUMNS = BASE_COLUMNS + ("θ1i", "θ2i", "B1i", "B2i")
FROLICHX2_COLUMNS = BASE_COLUMNS + ("J1i", "J2i")
FROLICHX4_COLUMNS = FROLICHX2_COLUMNS + ("N1i", "N2i")
WESTERGAARD_COLUMNS = BASE_COLUMNS + ("θ1i", "θ2i", "W1i", "W2i")


def concat_dszi(tupla) -> tuple[str]:
    return tupla + tuple(["σzi"])


COLUMN_DICTIONARY: dict[MetodosCalculo, tuple] = {
    MetodosCalculo.BOUSSINESQ_X3: list(concat_dszi(BOUSSINESQ_COLUMNS)),
    MetodosCalculo.FROLICH_X2: list(concat_dszi(FROLICHX2_COLUMNS)),
    MetodosCalculo.FROLICH_X4: list(concat_dszi(FROLICHX4_COLUMNS)),
    MetodosCalculo.WESTERGAARD: list(concat_dszi(WESTERGAARD_COLUMNS)),
}


def get_columns(id: MetodosCalculo) -> list[str]:
    return COLUMN_DICTIONARY[id]


def BousinessqColumnsMapper(val: BoussinesqIterationResult) -> list[list[float]]:
    Xi = val.arista.puntoInicial.x
    Yi = val.arista.puntoInicial.y
    Xf = val.arista.puntoFinal.x
    Yf = val.arista.puntoFinal.y
    Li = val.arista.largo
    Fi = val.arista.F
    ai = val.arista.a
    C1i = val.arista.C1
    C2i = val.arista.C2
    q1i = val.q1i
    q12 = val.q2i
    B1i = val.B1i
    B2i = val.B2i
    Dszi = val.Dszi
    return [
        Xi,
        Yi,
        Xf,
        Yf,
        Li,
        Fi,
        ai,
        C1i,
        C2i,
        q1i,
        q12,
        B1i,
        B2i,
        Dszi,
    ]


def FrolichX2ColumnsMapper(val: FrolichX2IterationResult) -> list[list[float]]:
    Xi = val.arista.puntoInicial.x
    Yi = val.arista.puntoInicial.y
    Xf = val.arista.puntoFinal.x
    Yf = val.arista.puntoFinal.y
    Li = val.arista.largo
    Fi = val.arista.F
    ai = val.arista.a
    C1i = val.arista.C1
    C2i = val.arista.C2
    J1i = val.J1i
    J2i = val.J2i
    Dszi = val.Dszi
    return [
        Xi,
        Yi,
        Xf,
        Yf,
        Li,
        Fi,
        ai,
        C1i,
        C2i,
        J1i,
        J2i,
        Dszi,
    ]


def FrolichX4ColumnsMapper(val: FrolichX4IterationResult) -> list[list[float]]:
    Xi = val.arista.puntoInicial.x
    Yi = val.arista.puntoInicial.y
    Xf = val.arista.puntoFinal.x
    Yf = val.arista.puntoFinal.y
    Li = val.arista.largo
    Fi = val.arista.F
    ai = val.arista.a
    C1i = val.arista.C1
    C2i = val.arista.C2
    J1i = val.J1i
    J2i = val.J2i
    N1 = val.N1i
    N2 = val.N2i
    Dszi = val.Dszi
    return [Xi, Yi, Xf, Yf, Li, Fi, ai, C1i, C2i, J1i, J2i, N1, N2, Dszi]


def WestergaardColumnsMapper(val: WestergaardIterationResult) -> list[list[float]]:
    Xi = val.arista.puntoInicial.x
    Yi = val.arista.puntoInicial.y
    Xf = val.arista.puntoFinal.x
    Yf = val.arista.puntoFinal.y
    Li = val.arista.largo
    Fi = val.arista.F
    ai = val.arista.a
    C1i = val.arista.C1
    C2i = val.arista.C2
    q1i = val.q1i
    q12 = val.q2i
    W1i = val.W1i
    W2i = val.W2i
    Dszi = val.Dszi
    return [
        Xi,
        Yi,
        Xf,
        Yf,
        Li,
        Fi,
        ai,
        C1i,
        C2i,
        q1i,
        q12,
        W1i,
        W2i,
        Dszi,
    ]


COLUMN_MAPPERS = {
    MetodosCalculo.BOUSSINESQ_X3: BousinessqColumnsMapper,
    MetodosCalculo.FROLICH_X2: FrolichX2ColumnsMapper,
    MetodosCalculo.FROLICH_X4: FrolichX4ColumnsMapper,
    MetodosCalculo.WESTERGAARD: WestergaardColumnsMapper,
}


class StressIncrementResultsToDataGridParser:
    @staticmethod
    def getDataGrid(
        methodo: MetodosCalculo, iterations: list[IterationUnionResults]
    ) -> list[list[float]]:
        values = map(COLUMN_MAPPERS[methodo], iterations)
        return list(values)
    
    @staticmethod
    def getColumns(methodo: MetodosCalculo):
        return get_columns(methodo)
