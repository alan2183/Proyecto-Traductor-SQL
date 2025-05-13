from antlr4 import *  # Importa las clases base de ANTLR
from ConsultaSQLLexer import ConsultaSQLLexer  # Lexer generado por ANTLR
from ConsultaSQLParser import ConsultaSQLParser  # Parser generado por ANTLR
from ConsultaSQLVisitor import ConsultaSQLVisitor  # Visitante base generado por ANTLR

# Clase que extiende del Visitor para traducir las instrucciones al SQL correspondiente
class TraductorSQLVisitor(ConsultaSQLVisitor):

    # Traduce consultas tipo: MOSTRAR PRODUCTOS [CON CAMPO COMPARADOR VALOR]
    def visitMostrar(self, ctx):
        tabla = ctx.ID().getText()  # Obtiene el nombre de la tabla

        # Si hay una condición (ej. CON PRECIO MAYOR A 1000)
        if ctx.condicion():
            campo = ctx.condicion().ID().getText()  # Campo a comparar, ej: PRECIO
            comp = ctx.condicion().comparador().getText()  # Comparador en texto (ej. MAYOR A)
            valor = ctx.condicion().valor().getText()  # Valor a comparar, ej: 1000

            # Diccionario que traduce del español al operador SQL
            operador = {
                'MAYOR A': '>',
                'MENOR A': '<',
                'IGUAL A': '='
            }[comp]

            # Construye la consulta SQL final
            return f"SELECT * FROM {tabla} WHERE {campo} {operador} {valor};"

        # Si no hay condición, simplemente seleccionatodo
        return f"SELECT * FROM {tabla};"

    # Traduce: CONTAR PRODUCTOS
    def visitContar(self, ctx):
        tabla = ctx.ID().getText()  # Obtiene el nombre de la tabla
        return f"SELECT COUNT(*) FROM {tabla};"

    # Traduce: BORRAR PRODUCTOS DONDE ID IGUAL A 5
    def visitBorrar(self, ctx):
        tabla = ctx.ID(0).getText()     # Primer ID: nombre de la tabla
        campo = ctx.ID(1).getText()     # Segundo ID: nombre del campo (ej. ID)
        valor = ctx.NUM().getText()     # Número (ej. 5)
        return f"DELETE FROM {tabla} WHERE {campo} = {valor};"

# Función principal que traduce texto en español a SQL usando el Visitor
def traducir(instruccion):
    # Crea un flujo de entrada desde el texto en español
    input_stream = InputStream(instruccion)

    # Genera tokens usando el lexer
    lexer = ConsultaSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Crea el parser usando los tokens
    parser = ConsultaSQLParser(stream)

    # Comienza desde la regla inicial: consulta
    tree = parser.consulta()

    # Instancia el visitor personalizado
    visitor = TraductorSQLVisitor()

    # Visita el árbol sintáctico y retorna la consulta SQL traducida
    return visitor.visit(tree)
