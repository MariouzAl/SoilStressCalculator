from enum import Enum


class MetodosCalculo(Enum):
        BOUSSINESQ_X3 = "χ=3 Boussinesq", 1
        FROLICH_X2 = "χ=2 Frolich", 2
        FROLICH_X4 = "χ=4 Frolich",3
        WESTERGAARD= "χ=1.5 WESTERGAARD",4