# Generated from C:/Users/chofi/PycharmProjects/traductor_sql/ConsultaSQL.g4 by ANTLR 4.13.2

from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

# Esta función representa la versión serializada del autómata léxico generado.
# Básicamente, es una codificación que ANTLR usa para construir el autómata
# que reconocerá los tokens del lenguaje.

# Aquí esta un montón de números que representan los estados y transiciones del lexer
def serializedATN():
    return [
        4,0,12,102,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,4,9,87,8,9,11,9,12,9,88,
        1,10,4,10,92,8,10,11,10,12,10,93,1,11,4,11,97,8,11,11,11,12,11,98,
        1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,12,1,0,3,1,0,65,90,1,0,48,57,3,0,9,10,13,13,32,32,104,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,33,1,0,0,0,5,40,1,0,0,0,7,47,1,0,
        0,0,9,53,1,0,0,0,11,57,1,0,0,0,13,61,1,0,0,0,15,69,1,0,0,0,17,77,
        1,0,0,0,19,86,1,0,0,0,21,91,1,0,0,0,23,96,1,0,0,0,25,26,5,77,0,0,
        26,27,5,79,0,0,27,28,5,83,0,0,28,29,5,84,0,0,29,30,5,82,0,0,30,31,
        5,65,0,0,31,32,5,82,0,0,32,2,1,0,0,0,33,34,5,67,0,0,34,35,5,79,0,
        0,35,36,5,78,0,0,36,37,5,84,0,0,37,38,5,65,0,0,38,39,5,82,0,0,39,
        4,1,0,0,0,40,41,5,66,0,0,41,42,5,79,0,0,42,43,5,82,0,0,43,44,5,82,
        0,0,44,45,5,65,0,0,45,46,5,82,0,0,46,6,1,0,0,0,47,48,5,68,0,0,48,
        49,5,79,0,0,49,50,5,78,0,0,50,51,5,68,0,0,51,52,5,69,0,0,52,8,1,
        0,0,0,53,54,5,83,0,0,54,55,5,69,0,0,55,56,5,65,0,0,56,10,1,0,0,0,
        57,58,5,67,0,0,58,59,5,79,0,0,59,60,5,78,0,0,60,12,1,0,0,0,61,62,
        5,77,0,0,62,63,5,65,0,0,63,64,5,89,0,0,64,65,5,79,0,0,65,66,5,82,
        0,0,66,67,5,32,0,0,67,68,5,65,0,0,68,14,1,0,0,0,69,70,5,77,0,0,70,
        71,5,69,0,0,71,72,5,78,0,0,72,73,5,79,0,0,73,74,5,82,0,0,74,75,5,
        32,0,0,75,76,5,65,0,0,76,16,1,0,0,0,77,78,5,73,0,0,78,79,5,71,0,
        0,79,80,5,85,0,0,80,81,5,65,0,0,81,82,5,76,0,0,82,83,5,32,0,0,83,
        84,5,65,0,0,84,18,1,0,0,0,85,87,7,0,0,0,86,85,1,0,0,0,87,88,1,0,
        0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,20,1,0,0,0,90,92,7,1,0,0,91,90,
        1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,22,1,0,0,0,
        95,97,7,2,0,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,
        0,0,0,99,100,1,0,0,0,100,101,6,11,0,0,101,24,1,0,0,0,4,0,88,93,98,
        1,6,0,0
    ]

# Clase principal del lexer, generado por ANTLR
class ConsultaSQLLexer(Lexer):

    # Aquí se construye el autómata a partir de la versión serializada
    atn = ATNDeserializer().deserialize(serializedATN())

    # Se crean las decisiones del DFA para el lexer
    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    # Definición de tokens por índice (internamente los usa ANTLR)
    T__0 = 1  # 'MOSTRAR'
    T__1 = 2  # 'CONTAR'
    T__2 = 3  # 'BORRAR'
    T__3 = 4  # 'DONDE'
    T__4 = 5  # 'SEA'
    T__5 = 6  # 'CON'
    T__6 = 7  # 'MAYOR A'
    T__7 = 8  # 'MENOR A'
    T__8 = 9  # 'IGUAL A'
    ID = 10  # Identificadores: solo letras mayúsculas (como nombres de tablas o campos)
    NUM = 11  # Números enteros positivos
    WS = 12  # Espacios en blanco (se ignoran)

    # Canales (por defecto y oculto, útil para tokens ignorados como WS)
    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    # Modos de operación del lexer (normalmente solo uno)
    modeNames = ["DEFAULT_MODE"]

    # Lista de los tokens literales (palabras clave del lenguaje)
    literalNames = ["<INVALID>",
                    "'MOSTRAR'", "'CONTAR'", "'BORRAR'", "'DONDE'", "'SEA'", "'CON'",
                    "'MAYOR A'", "'MENOR A'", "'IGUAL A'"]

    # Lista de los tokens simbólicos (tokens no literales como ID o NUM)
    symbolicNames = ["<INVALID>",
                     "ID", "NUM", "WS"]

    # Lista de reglas léxicas: define cómo se reconocen los tokens
    ruleNames = ["T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6",
                 "T__7", "T__8", "ID", "NUM", "WS"]

    # Nombre del archivo original de gramática de ANTLR
    grammarFileName = "ConsultaSQL.g4"

    # Constructor del lexer
    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")  # Asegura que la versión sea compatible
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


