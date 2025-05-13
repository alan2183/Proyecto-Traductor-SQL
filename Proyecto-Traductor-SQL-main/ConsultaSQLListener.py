# Generated from C:/Users/chofi/PycharmProjects/traductor_sql/ConsultaSQL.g4 by ANTLR 4.13.2

from antlr4 import *

# Importamos el parser correspondiente. Esta verificación con "__name__" permite
# que este archivo funcione correctamente tanto como script directo como módulo importado.
if "." in __name__:
    from .ConsultaSQLParser import ConsultaSQLParser
else:
    from ConsultaSQLParser import ConsultaSQLParser

# Esta clase es un "listener", es decir, una clase que puede reaccionar
# cuando el parser entra o sale de ciertas reglas gramaticales.
# Es una herramienta útil si quieres realizar acciones al recorrer el árbol de análisis sintáctico.
class ConsultaSQLListener(ParseTreeListener):

    # Este método se ejecuta al ENTRAR en un nodo que representa la regla 'consulta'.
    def enterConsulta(self, ctx:ConsultaSQLParser.ConsultaContext):
        pass  # Aquí puedes poner lógica personalizada al entrar a 'consulta'

    # Este método se ejecuta al SALIR de un nodo que representa la regla 'consulta'.
    def exitConsulta(self, ctx:ConsultaSQLParser.ConsultaContext):
        pass  # Aquí puedes poner lógica personalizada al salir de 'consulta'

    # Lo mismo para la regla 'mostrar'
    def enterMostrar(self, ctx:ConsultaSQLParser.MostrarContext):
        pass

    def exitMostrar(self, ctx:ConsultaSQLParser.MostrarContext):
        pass

    # Para la regla 'contar'
    def enterContar(self, ctx:ConsultaSQLParser.ContarContext):
        pass

    def exitContar(self, ctx:ConsultaSQLParser.ContarContext):
        pass

    # Para la regla 'borrar'
    def enterBorrar(self, ctx:ConsultaSQLParser.BorrarContext):
        pass

    def exitBorrar(self, ctx:ConsultaSQLParser.BorrarContext):
        pass

    # Para la regla 'condicion'
    def enterCondicion(self, ctx:ConsultaSQLParser.CondicionContext):
        pass

    def exitCondicion(self, ctx:ConsultaSQLParser.CondicionContext):
        pass

    # Para la regla 'comparador' (como MAYOR A, MENOR A, IGUAL A)
    def enterComparador(self, ctx:ConsultaSQLParser.ComparadorContext):
        pass

    def exitComparador(self, ctx:ConsultaSQLParser.ComparadorContext):
        pass

    # Para la regla 'valor' (puede ser un número o identificador)
    def enterValor(self, ctx:ConsultaSQLParser.ValorContext):
        pass

    def exitValor(self, ctx:ConsultaSQLParser.ValorContext):
        pass

# Al final se elimina la referencia al parser para no dejar residuos en el namespace global.
del ConsultaSQLParser
