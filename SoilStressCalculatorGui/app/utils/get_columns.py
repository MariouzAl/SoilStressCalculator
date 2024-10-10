from soil_vertical_stress_increment.models.methods_enum import MetodosCalculo


BASE_COLUMNS= ("Xi\'"	,"Yi\'",'Xf\'',"Yf\'",	"Li",	"Fi"	,"ai"	,"C1i"	,"C2i")
BOUSSINESQ_COLUMNS =BASE_COLUMNS + ("θ1i",	"θ2i"	,"B1i"	,"B2i")
FROLICHX2_COLUMNS= BASE_COLUMNS +("J1i"	,"J2i")
FROLICHX4_COLUMNS= FROLICHX2_COLUMNS +("N1i",	"N2i")
WESTERGAARD_COLUMNS= BASE_COLUMNS + ("θ1i",	"θ2i"	,"W1i"	,"W2i")
 

def concat_dszi(tupla)->tuple[str]:
        return tupla+tuple(['σzi'])


COLUMN_DICTIONARY:dict[MetodosCalculo,tuple]={
    MetodosCalculo.BOUSSINESQ_X3:list(concat_dszi(BOUSSINESQ_COLUMNS)),
    MetodosCalculo.FROLICH_X2:list(concat_dszi(FROLICHX2_COLUMNS)),
    MetodosCalculo.FROLICH_X4:list(concat_dszi(FROLICHX4_COLUMNS)),
    MetodosCalculo.WESTERGAARD:list(concat_dszi(WESTERGAARD_COLUMNS))
}

def get_columns(id:MetodosCalculo)->list[str]:
    return COLUMN_DICTIONARY[id]