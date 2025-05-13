# Generated from C:/Users/chofi/PycharmProjects/traductor_sql/ConsultaSQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,3,0,18,8,0,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        0,0,7,0,2,4,6,8,10,12,0,1,1,0,7,9,39,0,17,1,0,0,0,2,19,1,0,0,0,4,
        24,1,0,0,0,6,27,1,0,0,0,8,34,1,0,0,0,10,39,1,0,0,0,12,41,1,0,0,0,
        14,18,3,2,1,0,15,18,3,4,2,0,16,18,3,6,3,0,17,14,1,0,0,0,17,15,1,
        0,0,0,17,16,1,0,0,0,18,1,1,0,0,0,19,20,5,1,0,0,20,22,5,10,0,0,21,
        23,3,8,4,0,22,21,1,0,0,0,22,23,1,0,0,0,23,3,1,0,0,0,24,25,5,2,0,
        0,25,26,5,10,0,0,26,5,1,0,0,0,27,28,5,3,0,0,28,29,5,10,0,0,29,30,
        5,4,0,0,30,31,5,10,0,0,31,32,5,5,0,0,32,33,5,11,0,0,33,7,1,0,0,0,
        34,35,5,6,0,0,35,36,5,10,0,0,36,37,3,10,5,0,37,38,3,12,6,0,38,9,
        1,0,0,0,39,40,7,0,0,0,40,11,1,0,0,0,41,42,5,11,0,0,42,13,1,0,0,0,
        2,17,22
    ]

class ConsultaSQLParser ( Parser ):

    grammarFileName = "ConsultaSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MOSTRAR'", "'CONTAR'", "'BORRAR'", "'DONDE'", 
                     "'SEA'", "'CON'", "'MAYOR A'", "'MENOR A'", "'IGUAL A'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUM", "WS" ]

    RULE_consulta = 0
    RULE_mostrar = 1
    RULE_contar = 2
    RULE_borrar = 3
    RULE_condicion = 4
    RULE_comparador = 5
    RULE_valor = 6

    ruleNames =  [ "consulta", "mostrar", "contar", "borrar", "condicion", 
                   "comparador", "valor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    NUM=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ConsultaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mostrar(self):
            return self.getTypedRuleContext(ConsultaSQLParser.MostrarContext,0)


        def contar(self):
            return self.getTypedRuleContext(ConsultaSQLParser.ContarContext,0)


        def borrar(self):
            return self.getTypedRuleContext(ConsultaSQLParser.BorrarContext,0)


        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_consulta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsulta" ):
                listener.enterConsulta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsulta" ):
                listener.exitConsulta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsulta" ):
                return visitor.visitConsulta(self)
            else:
                return visitor.visitChildren(self)




    def consulta(self):

        localctx = ConsultaSQLParser.ConsultaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_consulta)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.mostrar()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.contar()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.borrar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MostrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ConsultaSQLParser.ID, 0)

        def condicion(self):
            return self.getTypedRuleContext(ConsultaSQLParser.CondicionContext,0)


        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_mostrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMostrar" ):
                listener.enterMostrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMostrar" ):
                listener.exitMostrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMostrar" ):
                return visitor.visitMostrar(self)
            else:
                return visitor.visitChildren(self)




    def mostrar(self):

        localctx = ConsultaSQLParser.MostrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mostrar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ConsultaSQLParser.T__0)
            self.state = 20
            self.match(ConsultaSQLParser.ID)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 21
                self.condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ConsultaSQLParser.ID, 0)

        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_contar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContar" ):
                listener.enterContar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContar" ):
                listener.exitContar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContar" ):
                return visitor.visitContar(self)
            else:
                return visitor.visitChildren(self)




    def contar(self):

        localctx = ConsultaSQLParser.ContarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_contar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ConsultaSQLParser.T__1)
            self.state = 25
            self.match(ConsultaSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BorrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConsultaSQLParser.ID)
            else:
                return self.getToken(ConsultaSQLParser.ID, i)

        def NUM(self):
            return self.getToken(ConsultaSQLParser.NUM, 0)

        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_borrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBorrar" ):
                listener.enterBorrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBorrar" ):
                listener.exitBorrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBorrar" ):
                return visitor.visitBorrar(self)
            else:
                return visitor.visitChildren(self)




    def borrar(self):

        localctx = ConsultaSQLParser.BorrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_borrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ConsultaSQLParser.T__2)
            self.state = 28
            self.match(ConsultaSQLParser.ID)
            self.state = 29
            self.match(ConsultaSQLParser.T__3)
            self.state = 30
            self.match(ConsultaSQLParser.ID)
            self.state = 31
            self.match(ConsultaSQLParser.T__4)
            self.state = 32
            self.match(ConsultaSQLParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ConsultaSQLParser.ID, 0)

        def comparador(self):
            return self.getTypedRuleContext(ConsultaSQLParser.ComparadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(ConsultaSQLParser.ValorContext,0)


        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = ConsultaSQLParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ConsultaSQLParser.T__5)
            self.state = 35
            self.match(ConsultaSQLParser.ID)
            self.state = 36
            self.comparador()
            self.state = 37
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_comparador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparador" ):
                listener.enterComparador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparador" ):
                listener.exitComparador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparador" ):
                return visitor.visitComparador(self)
            else:
                return visitor.visitChildren(self)




    def comparador(self):

        localctx = ConsultaSQLParser.ComparadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ConsultaSQLParser.NUM, 0)

        def getRuleIndex(self):
            return ConsultaSQLParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = ConsultaSQLParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_valor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ConsultaSQLParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





