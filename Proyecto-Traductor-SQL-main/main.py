# main.py
from antlr4 import *
from ConsultaSQLLexer import ConsultaSQLLexer
from ConsultaSQLParser import ConsultaSQLParser
from ConsultaSQLVisitor import ConsultaSQLVisitor

class TraductorSQLVisitor(ConsultaSQLVisitor):
    def visitMostrar(self, ctx):
        tabla = ctx.ID().getText()
        if ctx.condicion():
            campo = ctx.condicion().ID().getText()
            comp = ctx.condicion().comparador().getText()
            valor = ctx.condicion().valor().getText()
            operador = {'MAYOR A': '>', 'MENOR A': '<', 'IGUAL A': '='}[comp]
            return f"SELECT * FROM {tabla} WHERE {campo} {operador} {valor};"
        return f"SELECT * FROM {tabla};"

    def visitContar(self, ctx):
        tabla = ctx.ID().getText()
        return f"SELECT COUNT(*) FROM {tabla};"

    def visitBorrar(self, ctx):
        tabla = ctx.ID(0).getText()
        campo = ctx.ID(1).getText()
        valor = ctx.NUM().getText()
        return f"DELETE FROM {tabla} WHERE {campo} = {valor};"

# Función para traducir la consulta
def traducir(instruccion):
    input_stream = InputStream(instruccion)
    lexer = ConsultaSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConsultaSQLParser(stream)
    tree = parser.consulta()

    visitor = TraductorSQLVisitor()
    return visitor.visit(tree)
