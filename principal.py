import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *

def procesar_imprimir(instr, ts) :
    print('> ', resolver_cadena(instr.cad, ts))
    #print(ts.simbolos)

def procesar_definicion(instr, ts) :
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)      # inicializamos con 0 como valor por defecto
    ts.agregar(simbolo)
    #print(ts.simbolos)

def procesar_asignacion(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    ts.actualizar(simbolo)

def procesar_mientras(instr, ts) :
    while resolver_expreision_logica(instr.expLogica, ts) :
        ts_local = TS.TablaDeSimbolos(ts.simbolos, ts.funciones)
        ret = procesar_instrucciones(instr.instrucciones, ts_local)
        if ret is not None:
            return ret

def procesar_if(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos, ts.funciones)
        return procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_if_else(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos, ts.funciones)
        return procesar_instrucciones(instr.instrIfVerdadero, ts_local)
    else :
        ts_local = TS.TablaDeSimbolos(ts.simbolos, ts.funciones)
        return procesar_instrucciones(instr.instrIfFalso, ts_local)

def procesar_if_elseif(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos, ts.funciones)
        return procesar_instrucciones(instr.instrucciones, ts_local)
    else :
        if isinstance(instr.elseif, If) : 
            ret = procesar_if(instr.elseif, ts)
            if ret is not None :
                return ret
        elif isinstance(instr.elseif, IfElse) : 
            ret = procesar_if_else(instr.elseif, ts)
            if ret is not None :
                return ret
        elif isinstance(instr.elseif, IfElseIf) : 
            ret = procesar_if_elseif(instr.elseif, ts)
            if ret is not None :
                return ret


def procesar_funcion(instr, ts) :
    funcion = TS.Funciones(instr.id, instr.parametros, instr.instrucciones)
    ts.agregar_funcion(funcion)

def procesar_llamada(instr, ts) :
    ts_local = TS.TablaDeSimbolos(ts.simbolos, ts.funciones)

    funcion = ts.obtener_funcion(instr.id)

    if len(funcion.parametros) == len(instr.parametros) :

        for par in enumerate(funcion.parametros) :
            val = resolver_expresion_aritmetica(instr.parametros[par[0]], ts)
            #print(par.id, " = ", val)
            simbolo = TS.Simbolo(par[1].id, TS.TIPO_DATO.NUMERO, val)
            ts_local.agregar(simbolo)
        
        return procesar_instrucciones(funcion.instrucciones, ts_local)
    else :
        print('Error: cantidad de parametros no erronea')

def procesar_retorno(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expresion, ts)
    return val

def resolver_cadena(expCad, ts) :
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')


def resolver_expreision_logica(expLog, ts) :
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor
    elif isinstance(expNum, ExpresionFuncion) :
        return procesar_llamada(expNum, ts)


def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
        elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
        elif isinstance(instr, Mientras) : 
            ret = procesar_mientras(instr, ts)
            if ret is not None :
                return ret
        elif isinstance(instr, If) : 
            ret = procesar_if(instr, ts)
            if ret is not None :
                return ret
        elif isinstance(instr, IfElse) : 
            ret = procesar_if_else(instr, ts)
            if ret is not None :
                return ret
        elif isinstance(instr, Funcion) : procesar_funcion(instr, ts)
        elif isinstance(instr, LlamadaFuncion) : procesar_llamada(instr, ts)
        elif isinstance(instr, Retorno) : return procesar_retorno(instr, ts)
        elif isinstance(instr, IfElseIf) : 
            ret = procesar_if_elseif(instr, ts)
            if ret is not None :
                return ret
        else : print('Error: instrucción no válida')

f = open("./entrada2.txt", "r")
input = f.read()

f.close()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global)

#print(instrucciones)
#print(ts_global.simbolos)