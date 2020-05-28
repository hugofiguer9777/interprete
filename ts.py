from enum import Enum

class TIPO_DATO(Enum) :
    NUMERO = 1

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor

class Funciones() :
    'Esta clase representa las funciones dentro de nuestra tabla de simbolos'

    def __init__(self, id, parametros = [], instrucciones = []) :
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}, funciones = {}) :
        self.simbolos = simbolos.copy()
        self.funciones = funciones.copy()

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            print('Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            print('Error: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id].tipo = simbolo.tipo
            self.simbolos[simbolo.id].valor = simbolo.valor
            #self.simbolos[simbolo.id] = simbolo

    def agregar_funcion(self, funcion) :
        self.funciones[funcion.id] = funcion
    
    def obtener_funcion(self, id) :
        if not id in self.funciones :
            print('Error: funcion ', id, ' no definida.')

        return self.funciones[id]