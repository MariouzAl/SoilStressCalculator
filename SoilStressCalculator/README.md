# SoilStressCalculator

Proyecto de Caluladora de distribucion de esfuerzo vertical dentro de la masa de suelo por efecto de una carga uniformemente 

## Metodos de calculo 
* Boussinesq(χ=3)
* Frolich(χ2)
* Frolich(χ4)

## Modulos Principales
* `main.py` : Modulo que ejecuta la rutina con datos de prueba 
* `calculator.py` : Modulo que contiene las clases :        
    * `SoilStressCalculator`, 
    * `Boussinesq`, 
    * `FrolichX2`, 
    * `FrolichX4`
* `poligono.py` Modulo que contiene la clase: 
    * `Poligono` 
* `arista.py` : Modulo que contiene las clases: 
    * `Arista` 
    * `AristaWrapper`
* `punto.py` : Modulo que contiene las clases :
    * `Punto2D`
    * `Punto3D`
    * `CalculadoraPuntoPrimo`
* `reducers`
    * `boussinesq_reducer.py` :
        * funciones reducer : 
            * `BoussinesqReducer`
    * `frolich_reducer.py`: 
        * funciones reducer : 
            * `FrolichX2Reducer`
            * `FrolichX4Reducer` 


## Clases 

### SoilStressCalculator
Clase base de las clases `Boussinesq`, `FrolichX2`, `FrolichX4`, `Westergaard`(Trabajo en progreso)

Se encarga de hacer los calculos de acuerdo a la estrategia que se le pase como parametro en el contructor ( `__init__` )

> <strong style="color:red; font-weigth:bold">NOTA: se utiliza la funcion REDUCE, como estrategia de calculo, porque en un diseño original no se consideraba que se utilizarian los valores de las iteraciones y solo se buscaba obtener el valor final. Con base a la retroalimentacion, se considera mejor utilizar una funcion MAP que devuelva una lista con los diferentes valores calculados. Razon por la cual se deberan cambiar las funciones reducer a funciones map </strong>

#### Propiedades 
* `NAME`:str
* `q`:float
* `P`:float
* `vertices` :list[Punto2D]
* `poligono`: Poligono
* `strategy` : Callable[[float],Callable[[float,AristaWrapper],float]]

#### Metodos 
* `__init__`: Contructor que se encarga de inicializar las propiedades de la calculadora, asi como de calcular los valores de los vertices primos. Recibe como parametros : 
    * q: float, 
    * P : Punto3D, 
    * vertices :list[Punto2D], 
    * strategy : Callable[[float],Callable[[float,AristaWrapper],float]] 
* `calculate`: Se encarga de calcular el valor del estres
* `__calcVerticesPrimos`: Genera los vertices primos con respecto al punto P

### Boussinesq
Clase que hereda de la clase `SoilStressCalculator` asigna la estrategia `BoussinesqReducer`

### FrolichX2
Clase que hereda de la clase `SoilStressCalculator` asigna la estrategia `FrolichX2Reducer`
### FrolichX4
Clase que hereda de la clase `SoilStressCalculator` asigna la estrategia `FrolichX4Reducer`

### Poligono
Clase que se encarga de recibir una lista de vertices y el valor Z del punto P
se encarga de calcular las aristas que se forman con la lista de vertices 


#### Propiedades
* `__aristas`:`list[Arista]=[]`
* `__Zp `:`float` 
#### Metodos 
* `__init__`: Constructor que se encarga de calcular las aristas.Recibe como parametros :
    * vertices:list[Punto2D],
    * Zp=0
* `_calcAristas`: Calcula las aristas con base a los vertices devuelve una lista de objetos `AristaWrapper`

### Arista
Clase que guarda la referencia de dos puntos (`Punto2D`) : el punto inicial y el punto final, calcula el `largo`(distancia entre ambos puntos)  y el valor `F`

### AristaWrapper

Clase que extiende(hereda) de la clase `Arista` recibe como parametro en el contructor un objeto de la clase arista y el valor `z` de `P` se encarga de calcular :
* `_a`
* `_C1`
* `_C2`

### Punto2D
Clase que representa un punto bidimencional de coordenadas x,y

### Punto3D
Clase que hereda de `Punto2D` y agrega la coordenada z

### CalculadoraPuntoPrimo
Clase  que contiene el metodo estatico `crearPuntoPrimo` que calcula el punto primo respecto a P 
Recibe como parametros  dos punto 2D .

> Nota : Recordar que la clase `Punto3D` hereda de `Punto2D` por lo que tambien se puede pasar como parametro. De hecho esta es la implementacion que se hace al pasarle como parametro el punto P(objeto de la clase Punto3D) para calcular los puntos primos de los vertices 

## Funciones reducer(Work in Progress)
Las funciones reducer siguen un patrón de *closure* (**High Order Function** ), en el que se define una funcion que al ejecutarse devuelve otra funcion que posteriormente se ejecutara

Esto nos permite pasarle valores adicionales a las funciones en el caso del ejemplo de `BoussinesqReducer` y `FrolichReducer` necesitamos pasar `valorSobrecarga`  para que la funcion reducer pueda hacer los calculos. Para un futuro reducer de `Wertergaard` podria requerir la `Relacion de poisson` o el valor de `k` dependiendo como se quiera implementar  

``` Python
def BoussinesqReducer(valorSobrecarga:float)->Callable[[float,AristaWrapper],float]:
    def reducerFunction(acc:float,arista:AristaWrapper)->float:
            ...
            Dszi =((valorSobrecarga)/((2)*(pi)))...
            return acc+Dszi

    def caclB(a,c):
        return (a*c)/(sqrt((1)+(a**2)+(c**2)))
    return reducerFunction
```

Como se mencionó previamente, este diseño deberá cambiar ya que el diseño original sólo consideraba relevante obtener el valor final más no los resultados de las iteraciones; sin embargo, se seguira utilizando el mismo patrón de *closure* (**High Order Function** ) ya que sólo se necesita cambiar de una funcion `reduce` a una funcion `map` (ya que trabajan de manera similar iterando sobre listas) y que tambien necesita una funcion como parametro.
El cambio mas notable sera que la funcion que devuelva ya no tendra el parametro del accumulador(acc) solamente debe recibir el parametro de la arista en turno.

En la  clase `SoilStressCalculator` en el metodo `__calcVerticesPrimos` tenemos un ejemplo del uso de la funcion `map`  solo que en lugar de usar una funcion que se define con la palabra reservada `def` tenemos una implementacion con una fucion `lambda` donde se itera la lista de `vertices`  y por cada elemento `vertice` se ejecuta la funcion  `crearPuntoPrimo` que devuelve un objeto de la clase `Punto2D`

``` Python
 def __calcVerticesPrimos(self,vertices:list[Punto2D],P:Punto2D) -> list[Punto2D] : 
         return list(map(lambda vertice : CalculadoraPuntoPrimo.crearPuntoPrimo(vertice,P)  ,vertices))
```

En nuestra conversion de funcion reducer  a funcion map lo que podriamos devolver es un objeto diccionario con los valores calculados


[Ir a menu principal](../README.md)