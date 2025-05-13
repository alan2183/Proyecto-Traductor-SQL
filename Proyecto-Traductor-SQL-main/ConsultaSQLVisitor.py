# Generated from C:/Users/chofi/PycharmProjects/traductor_sql/ConsultaSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ConsultaSQLParser import ConsultaSQLParser
else:
    from ConsultaSQLParser import ConsultaSQLParser

# This class defines a complete generic visitor for a parse tree produced by ConsultaSQLParser.

class ConsultaSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConsultaSQLParser#consulta.
    def visitConsulta(self, ctx:ConsultaSQLParser.ConsultaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConsultaSQLParser#mostrar.
    def visitMostrar(self, ctx:ConsultaSQLParser.MostrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConsultaSQLParser#contar.
    def visitContar(self, ctx:ConsultaSQLParser.ContarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConsultaSQLParser#borrar.
    def visitBorrar(self, ctx:ConsultaSQLParser.BorrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConsultaSQLParser#condicion.
    def visitCondicion(self, ctx:ConsultaSQLParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConsultaSQLParser#comparador.
    def visitComparador(self, ctx:ConsultaSQLParser.ComparadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConsultaSQLParser#valor.
    def visitValor(self, ctx:ConsultaSQLParser.ValorContext):
        return self.visitChildren(ctx)



del ConsultaSQLParser