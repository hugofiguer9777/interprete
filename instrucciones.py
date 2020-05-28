class Instruccion:
    '''This is an abstract class'''

class Imprimir(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad

class Mientras(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class Definicion(Instruccion) :
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    '''

    def __init__(self, id) :
        self.id = id

class Asignacion(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, expNumerica) :
        self.id = id
        self.expNumerica = expNumerica

class If(Instruccion) : 
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class IfElse(Instruccion) : 
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = []) :
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso

class IfElseIf(Instruccion) :
    '''
        Esta clase representa la instrucción if-elseif.
        La instrucción if-elseif recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones if
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica, elseif, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        self.elseif = elseif

class Funcion(Instruccion) :
    '''
        Esta clase representa la instrucción de una función.
        La instrucción función recibe como parametros el id, una lista de parametros que usará dentro de la función y
        una lista de instrucciones a ejecutar dentro de la funcion
    '''

    def __init__(self, id, parametros = [], instrucciones = []) :
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones

class Parametro(Instruccion) :
    '''
        Esta clase representa la instrucción de definición de un parametro de una función.
        Recibe como parámetro el nombre del identificador a definir
    '''

    def __init__(self, id) :
        self.id = id

class LlamadaFuncion(Instruccion) :
    '''
        Esta clase representa la instrucción de una llamada a función.
        La instrucción función recibe como parametros el id, una lista de parametros que 
        definiran a la función.
    '''

    def __init__(self, id, parametros = []) :
        self.id = id
        self.parametros = parametros

class Retorno(Instruccion) :
    '''
        Esta clase representa la instruccion de retorno de una función.
        La instrucción retorno recibe como parametros una expresion la cual va a retornar.
    '''

    def __init__(self, expresion) :
        self.expresion = expresion