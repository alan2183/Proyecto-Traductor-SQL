# Generated from C:/Users/chofi/PycharmProjects/traductor_sql/ConsultaSQL.g4 by ANTLR 4.13.2

from antlr4 import *

# Verificamos si este archivo se está ejecutando como script o como parte de un paquete.
# Esto permite que el import funcione correctamente en ambos casos.
if "." in __name__:
    from .ConsultaSQLParser import ConsultaSQLParser
else:
    from ConsultaSQLParser import ConsultaSQLParser

# Esta clase define un "Visitor" genérico para el árbol de análisis producido por ConsultaSQLParser.
# A diferencia del Listener, el Visitor devuelve explícitamente resultados al visitar cada nodo.
# Esto es útil si necesitas construir estructuras, interpretar o transformar el árbol.
class ConsultaSQLVisitor(ParseTreeVisitor):

    # Visita un nodo del árbol que representa la regla 'consulta'.
    # El método 'visitChildren' recorre automáticamente todos los hijos del nodo.
    def visitConsulta(self, ctx:ConsultaSQLParser.ConsultaContext):
        return self.visitChildren(ctx)

    # Visita un nodo que representa la regla 'mostrar' (ej: MOSTRAR empleados)
    def visitMostrar(self, ctx:ConsultaSQLParser.MostrarContext):
        return self.visitChildren(ctx)

    # Visita un nodo de tipo 'contar' (ej: CONTAR empleados)
    def visitContar(self, ctx:ConsultaSQLParser.ContarContext):
        return self.visitChildren(ctx)

    # Visita un nodo de tipo 'borrar' (ej: BORRAR empleados)
    def visitBorrar(self, ctx:ConsultaSQLParser.BorrarContext):
        return self.visitChildren(ctx)

    # Visita un nodo de tipo 'condicion' (ej: DONDE edad MAYOR A 30)
    def visitCondicion(self, ctx:ConsultaSQLParser.CondicionContext):
        return self.visitChildren(ctx)

    # Visita un nodo de tipo 'comparador' (ej: MAYOR A, MENOR A, IGUAL A)
    def visitComparador(self, ctx:ConsultaSQLParser.ComparadorContext):
        return self.visitChildren(ctx)

    # Visita un nodo de tipo 'valor', que puede ser una cadena, número, etc.
    def visitValor(self, ctx:ConsultaSQLParser.ValorContext):
        return self.visitChildren(ctx)

# Se elimina la referencia a ConsultaSQLParser del espacio de nombres global.
del ConsultaSQLParser
