# Generated from DE6Parser.g4 by ANTLR 4.11.1
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
        4,1,38,254,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,3,0,66,8,0,
        1,0,1,0,3,0,70,8,0,1,0,1,0,1,0,1,0,5,0,76,8,0,10,0,12,0,79,9,0,1,
        0,3,0,82,8,0,1,0,1,0,3,0,86,8,0,1,1,3,1,89,8,1,1,1,4,1,92,8,1,11,
        1,12,1,93,1,2,1,2,1,2,1,2,1,2,1,2,3,2,102,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,110,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,3,8,129,8,8,1,9,1,9,1,10,1,10,3,10,135,8,10,
        1,11,1,11,1,11,5,11,140,8,11,10,11,12,11,143,9,11,1,12,1,12,1,12,
        3,12,148,8,12,1,12,1,12,1,13,1,13,1,13,3,13,155,8,13,1,13,1,13,1,
        14,1,14,1,14,1,15,1,15,1,15,3,15,165,8,15,1,16,1,16,1,16,1,16,1,
        16,1,16,3,16,173,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,197,8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,
        24,1,24,3,24,210,8,24,1,25,1,25,3,25,214,8,25,1,26,1,26,3,26,218,
        8,26,1,26,3,26,221,8,26,1,27,1,27,3,27,225,8,27,1,27,1,27,1,27,4,
        27,230,8,27,11,27,12,27,231,1,27,1,27,3,27,236,8,27,3,27,238,8,27,
        1,28,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,2,1,0,13,16,2,0,8,8,
        30,30,259,0,85,1,0,0,0,2,91,1,0,0,0,4,101,1,0,0,0,6,109,1,0,0,0,
        8,111,1,0,0,0,10,115,1,0,0,0,12,119,1,0,0,0,14,121,1,0,0,0,16,128,
        1,0,0,0,18,130,1,0,0,0,20,134,1,0,0,0,22,136,1,0,0,0,24,144,1,0,
        0,0,26,151,1,0,0,0,28,158,1,0,0,0,30,164,1,0,0,0,32,166,1,0,0,0,
        34,174,1,0,0,0,36,178,1,0,0,0,38,180,1,0,0,0,40,196,1,0,0,0,42,198,
        1,0,0,0,44,202,1,0,0,0,46,204,1,0,0,0,48,209,1,0,0,0,50,213,1,0,
        0,0,52,220,1,0,0,0,54,237,1,0,0,0,56,239,1,0,0,0,58,243,1,0,0,0,
        60,245,1,0,0,0,62,249,1,0,0,0,64,66,3,2,1,0,65,64,1,0,0,0,65,66,
        1,0,0,0,66,67,1,0,0,0,67,86,5,0,0,1,68,70,3,2,1,0,69,68,1,0,0,0,
        69,70,1,0,0,0,70,71,1,0,0,0,71,77,3,4,2,0,72,73,3,2,1,0,73,74,3,
        4,2,0,74,76,1,0,0,0,75,72,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,
        78,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,80,82,3,2,1,0,81,80,1,0,0,
        0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,5,0,0,1,84,86,1,0,0,0,85,65,
        1,0,0,0,85,69,1,0,0,0,86,1,1,0,0,0,87,89,5,33,0,0,88,87,1,0,0,0,
        88,89,1,0,0,0,89,90,1,0,0,0,90,92,5,34,0,0,91,88,1,0,0,0,92,93,1,
        0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,3,1,0,0,0,95,102,3,6,3,0,96,
        102,3,32,16,0,97,102,3,40,20,0,98,102,3,42,21,0,99,102,3,44,22,0,
        100,102,3,46,23,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,101,
        98,1,0,0,0,101,99,1,0,0,0,101,100,1,0,0,0,102,5,1,0,0,0,103,110,
        3,10,5,0,104,110,3,8,4,0,105,110,3,28,14,0,106,110,3,38,19,0,107,
        110,3,24,12,0,108,110,3,30,15,0,109,103,1,0,0,0,109,104,1,0,0,0,
        109,105,1,0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,1,0,0,0,
        110,7,1,0,0,0,111,112,3,12,6,0,112,113,5,18,0,0,113,114,3,14,7,0,
        114,9,1,0,0,0,115,116,3,12,6,0,116,117,5,17,0,0,117,118,3,14,7,0,
        118,11,1,0,0,0,119,120,3,54,27,0,120,13,1,0,0,0,121,122,3,16,8,0,
        122,15,1,0,0,0,123,129,3,20,10,0,124,129,5,35,0,0,125,129,3,54,27,
        0,126,129,3,26,13,0,127,129,3,18,9,0,128,123,1,0,0,0,128,124,1,0,
        0,0,128,125,1,0,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,17,1,0,0,
        0,130,131,5,32,0,0,131,19,1,0,0,0,132,135,5,30,0,0,133,135,5,31,
        0,0,134,132,1,0,0,0,134,133,1,0,0,0,135,21,1,0,0,0,136,141,3,16,
        8,0,137,138,5,11,0,0,138,140,3,16,8,0,139,137,1,0,0,0,140,143,1,
        0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,23,1,0,0,0,143,141,1,0,
        0,0,144,145,5,32,0,0,145,147,5,26,0,0,146,148,3,22,11,0,147,146,
        1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,27,0,0,150,25,
        1,0,0,0,151,152,5,32,0,0,152,154,5,26,0,0,153,155,3,22,11,0,154,
        153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,157,5,27,0,0,157,
        27,1,0,0,0,158,159,5,29,0,0,159,160,3,12,6,0,160,29,1,0,0,0,161,
        162,5,12,0,0,162,165,3,14,7,0,163,165,5,12,0,0,164,161,1,0,0,0,164,
        163,1,0,0,0,165,31,1,0,0,0,166,167,3,34,17,0,167,168,5,6,0,0,168,
        169,3,6,3,0,169,172,1,0,0,0,170,171,5,7,0,0,171,173,3,6,3,0,172,
        170,1,0,0,0,172,173,1,0,0,0,173,33,1,0,0,0,174,175,3,14,7,0,175,
        176,3,36,18,0,176,177,3,14,7,0,177,35,1,0,0,0,178,179,7,0,0,0,179,
        37,1,0,0,0,180,181,5,32,0,0,181,182,5,17,0,0,182,183,3,14,7,0,183,
        39,1,0,0,0,184,185,5,19,0,0,185,186,5,32,0,0,186,197,5,35,0,0,187,
        188,5,19,0,0,188,189,5,32,0,0,189,197,5,20,0,0,190,191,5,19,0,0,
        191,192,5,32,0,0,192,197,5,21,0,0,193,194,5,19,0,0,194,195,5,32,
        0,0,195,197,5,22,0,0,196,184,1,0,0,0,196,187,1,0,0,0,196,190,1,0,
        0,0,196,193,1,0,0,0,197,41,1,0,0,0,198,199,5,23,0,0,199,200,5,32,
        0,0,200,201,5,35,0,0,201,43,1,0,0,0,202,203,5,24,0,0,203,45,1,0,
        0,0,204,205,5,25,0,0,205,206,5,35,0,0,206,47,1,0,0,0,207,210,3,60,
        30,0,208,210,3,62,31,0,209,207,1,0,0,0,209,208,1,0,0,0,210,49,1,
        0,0,0,211,214,3,60,30,0,212,214,3,62,31,0,213,211,1,0,0,0,213,212,
        1,0,0,0,214,51,1,0,0,0,215,217,3,50,25,0,216,218,3,56,28,0,217,216,
        1,0,0,0,217,218,1,0,0,0,218,221,1,0,0,0,219,221,3,58,29,0,220,215,
        1,0,0,0,220,219,1,0,0,0,221,53,1,0,0,0,222,225,3,50,25,0,223,225,
        3,52,26,0,224,222,1,0,0,0,224,223,1,0,0,0,225,238,1,0,0,0,226,227,
        3,52,26,0,227,228,5,28,0,0,228,230,1,0,0,0,229,226,1,0,0,0,230,231,
        1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,235,1,0,0,0,233,236,
        3,50,25,0,234,236,3,52,26,0,235,233,1,0,0,0,235,234,1,0,0,0,236,
        238,1,0,0,0,237,224,1,0,0,0,237,229,1,0,0,0,238,55,1,0,0,0,239,240,
        5,26,0,0,240,241,7,1,0,0,241,242,5,27,0,0,242,57,1,0,0,0,243,244,
        5,9,0,0,244,59,1,0,0,0,245,246,5,1,0,0,246,247,5,11,0,0,247,248,
        5,3,0,0,248,61,1,0,0,0,249,250,5,2,0,0,250,251,5,11,0,0,251,252,
        5,4,0,0,252,63,1,0,0,0,25,65,69,77,81,85,88,93,101,109,128,134,141,
        147,154,164,172,196,209,213,217,220,224,231,235,237
    ]

class DE6Parser ( Parser ):

    grammarFileName = "DE6Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'?'", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "'echo'", "'='", "'!='", 
                     "'~'", "'!~'", "':='", "'?='", "'describe'", "'hidden'", 
                     "'const'", "'immutable'", "'export'", "'removeAllPrivateTags'", 
                     "'version'", "'['", "']'", "'/'", "'-'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'{'", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "PUBLIC_GROUP", "PVT_GROUP", "PUBLIC_ELEMENT", 
                      "PVT_ELEMENT", "HEXDIGIT_WILDCARD", "TEST_SYMBOL", 
                      "TEST_SEPERATOR", "ITEM_WILDCARD", "SEQ_WILDCARD", 
                      "WS", "COMMA", "ECHO", "EQUALS", "NOT_EQUALS", "MATCHES", 
                      "NOT_MATCHES", "ASSIGN", "ASSIGN_IF_EXISTS", "DESCRIBE", 
                      "HIDDEN_TOKEN", "CONST_TOKEN", "IMMUTABLE_TOKEN", 
                      "EXPORT", "REMOVE_ALL_PRIVATE_TAGS", "VERSION_WORD", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "SLASH", "DELETE_OPERATOR", 
                      "INTEGER", "FLOAT", "ID", "COMMENT", "NEWLINE", "STRING", 
                      "OPEN", "PVT_CREATOR_ID", "CLOSE" ]

    RULE_script = 0
    RULE_separator = 1
    RULE_statement = 2
    RULE_action = 3
    RULE_assign_if_exists = 4
    RULE_assignment = 5
    RULE_lvalue = 6
    RULE_value = 7
    RULE_term = 8
    RULE_variable = 9
    RULE_number = 10
    RULE_termlist = 11
    RULE_method = 12
    RULE_function_stmt = 13
    RULE_deletion = 14
    RULE_echo = 15
    RULE_conditional_statement = 16
    RULE_condition = 17
    RULE_conditionOperator = 18
    RULE_initialization = 19
    RULE_description = 20
    RULE_export_stmt = 21
    RULE_removeAllPrivateTags = 22
    RULE_version = 23
    RULE_tag = 24
    RULE_element = 25
    RULE_seq_element = 26
    RULE_tagpath = 27
    RULE_itemnumber = 28
    RULE_seq_wildcard = 29
    RULE_public_tag = 30
    RULE_pvt_tag = 31

    ruleNames =  [ "script", "separator", "statement", "action", "assign_if_exists", 
                   "assignment", "lvalue", "value", "term", "variable", 
                   "number", "termlist", "method", "function_stmt", "deletion", 
                   "echo", "conditional_statement", "condition", "conditionOperator", 
                   "initialization", "description", "export_stmt", "removeAllPrivateTags", 
                   "version", "tag", "element", "seq_element", "tagpath", 
                   "itemnumber", "seq_wildcard", "public_tag", "pvt_tag" ]

    EOF = Token.EOF
    PUBLIC_GROUP=1
    PVT_GROUP=2
    PUBLIC_ELEMENT=3
    PVT_ELEMENT=4
    HEXDIGIT_WILDCARD=5
    TEST_SYMBOL=6
    TEST_SEPERATOR=7
    ITEM_WILDCARD=8
    SEQ_WILDCARD=9
    WS=10
    COMMA=11
    ECHO=12
    EQUALS=13
    NOT_EQUALS=14
    MATCHES=15
    NOT_MATCHES=16
    ASSIGN=17
    ASSIGN_IF_EXISTS=18
    DESCRIBE=19
    HIDDEN_TOKEN=20
    CONST_TOKEN=21
    IMMUTABLE_TOKEN=22
    EXPORT=23
    REMOVE_ALL_PRIVATE_TAGS=24
    VERSION_WORD=25
    LEFT_BRACKET=26
    RIGHT_BRACKET=27
    SLASH=28
    DELETE_OPERATOR=29
    INTEGER=30
    FLOAT=31
    ID=32
    COMMENT=33
    NEWLINE=34
    STRING=35
    OPEN=36
    PVT_CREATOR_ID=37
    CLOSE=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DE6Parser.EOF, 0)

        def separator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DE6Parser.SeparatorContext)
            else:
                return self.getTypedRuleContext(DE6Parser.SeparatorContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DE6Parser.StatementContext)
            else:
                return self.getTypedRuleContext(DE6Parser.StatementContext,i)


        def getRuleIndex(self):
            return DE6Parser.RULE_script

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = DE6Parser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33 or _la==34:
                    self.state = 64
                    self.separator()


                self.state = 67
                self.match(DE6Parser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33 or _la==34:
                    self.state = 68
                    self.separator()


                self.state = 71
                self.statement()
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 72
                        self.separator()
                        self.state = 73
                        self.statement() 
                    self.state = 79
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33 or _la==34:
                    self.state = 80
                    self.separator()


                self.state = 83
                self.match(DE6Parser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(DE6Parser.NEWLINE)
            else:
                return self.getToken(DE6Parser.NEWLINE, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(DE6Parser.COMMENT)
            else:
                return self.getToken(DE6Parser.COMMENT, i)

        def getRuleIndex(self):
            return DE6Parser.RULE_separator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeparator" ):
                return visitor.visitSeparator(self)
            else:
                return visitor.visitChildren(self)




    def separator(self):

        localctx = DE6Parser.SeparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 87
                    self.match(DE6Parser.COMMENT)


                self.state = 90
                self.match(DE6Parser.NEWLINE)
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33 or _la==34):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(DE6Parser.ActionContext,0)


        def conditional_statement(self):
            return self.getTypedRuleContext(DE6Parser.Conditional_statementContext,0)


        def description(self):
            return self.getTypedRuleContext(DE6Parser.DescriptionContext,0)


        def export_stmt(self):
            return self.getTypedRuleContext(DE6Parser.Export_stmtContext,0)


        def removeAllPrivateTags(self):
            return self.getTypedRuleContext(DE6Parser.RemoveAllPrivateTagsContext,0)


        def version(self):
            return self.getTypedRuleContext(DE6Parser.VersionContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DE6Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.action()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.conditional_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.description()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.export_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.removeAllPrivateTags()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.version()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(DE6Parser.AssignmentContext,0)


        def assign_if_exists(self):
            return self.getTypedRuleContext(DE6Parser.Assign_if_existsContext,0)


        def deletion(self):
            return self.getTypedRuleContext(DE6Parser.DeletionContext,0)


        def initialization(self):
            return self.getTypedRuleContext(DE6Parser.InitializationContext,0)


        def method(self):
            return self.getTypedRuleContext(DE6Parser.MethodContext,0)


        def echo(self):
            return self.getTypedRuleContext(DE6Parser.EchoContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = DE6Parser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_action)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.assign_if_exists()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.deletion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.initialization()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.method()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.echo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_if_existsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(DE6Parser.LvalueContext,0)


        def ASSIGN_IF_EXISTS(self):
            return self.getToken(DE6Parser.ASSIGN_IF_EXISTS, 0)

        def value(self):
            return self.getTypedRuleContext(DE6Parser.ValueContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_assign_if_exists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_if_exists" ):
                return visitor.visitAssign_if_exists(self)
            else:
                return visitor.visitChildren(self)




    def assign_if_exists(self):

        localctx = DE6Parser.Assign_if_existsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_if_exists)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.lvalue()
            self.state = 112
            self.match(DE6Parser.ASSIGN_IF_EXISTS)
            self.state = 113
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(DE6Parser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(DE6Parser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(DE6Parser.ValueContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = DE6Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.lvalue()
            self.state = 116
            self.match(DE6Parser.ASSIGN)
            self.state = 117
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DE6Parser.RULE_lvalue

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TagpathLvalueContext(LvalueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.LvalueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tagpath(self):
            return self.getTypedRuleContext(DE6Parser.TagpathContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagpathLvalue" ):
                return visitor.visitTagpathLvalue(self)
            else:
                return visitor.visitChildren(self)



    def lvalue(self):

        localctx = DE6Parser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lvalue)
        try:
            localctx = DE6Parser.TagpathLvalueContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.tagpath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(DE6Parser.TermContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = DE6Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DE6Parser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TagPathTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tagpath(self):
            return self.getTypedRuleContext(DE6Parser.TagpathContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagPathTerm" ):
                return visitor.visitTagPathTerm(self)
            else:
                return visitor.visitChildren(self)


    class StringTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(DE6Parser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringTerm" ):
                return visitor.visitStringTerm(self)
            else:
                return visitor.visitChildren(self)


    class IdTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(DE6Parser.VariableContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdTerm" ):
                return visitor.visitIdTerm(self)
            else:
                return visitor.visitChildren(self)


    class NumberTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(DE6Parser.NumberContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberTerm" ):
                return visitor.visitNumberTerm(self)
            else:
                return visitor.visitChildren(self)


    class FunctionTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_stmt(self):
            return self.getTypedRuleContext(DE6Parser.Function_stmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionTerm" ):
                return visitor.visitFunctionTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = DE6Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = DE6Parser.NumberTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.number()
                pass

            elif la_ == 2:
                localctx = DE6Parser.StringTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(DE6Parser.STRING)
                pass

            elif la_ == 3:
                localctx = DE6Parser.TagPathTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.tagpath()
                pass

            elif la_ == 4:
                localctx = DE6Parser.FunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.function_stmt()
                pass

            elif la_ == 5:
                localctx = DE6Parser.IdTermContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DE6Parser.ID, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = DE6Parser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(DE6Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DE6Parser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntvalueContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(DE6Parser.INTEGER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntvalue" ):
                return visitor.visitIntvalue(self)
            else:
                return visitor.visitChildren(self)


    class FloatvalueContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(DE6Parser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatvalue" ):
                return visitor.visitFloatvalue(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = DE6Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_number)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                localctx = DE6Parser.IntvalueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(DE6Parser.INTEGER)
                pass
            elif token in [31]:
                localctx = DE6Parser.FloatvalueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(DE6Parser.FLOAT)
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


    class TermlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DE6Parser.TermContext)
            else:
                return self.getTypedRuleContext(DE6Parser.TermContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DE6Parser.COMMA)
            else:
                return self.getToken(DE6Parser.COMMA, i)

        def getRuleIndex(self):
            return DE6Parser.RULE_termlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermlist" ):
                return visitor.visitTermlist(self)
            else:
                return visitor.visitChildren(self)




    def termlist(self):

        localctx = DE6Parser.TermlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_termlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.term()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 137
                self.match(DE6Parser.COMMA)
                self.state = 138
                self.term()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DE6Parser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(DE6Parser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(DE6Parser.RIGHT_BRACKET, 0)

        def termlist(self):
            return self.getTypedRuleContext(DE6Parser.TermlistContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = DE6Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(DE6Parser.ID)
            self.state = 145
            self.match(DE6Parser.LEFT_BRACKET)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 41875931654) != 0:
                self.state = 146
                self.termlist()


            self.state = 149
            self.match(DE6Parser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DE6Parser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(DE6Parser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(DE6Parser.RIGHT_BRACKET, 0)

        def termlist(self):
            return self.getTypedRuleContext(DE6Parser.TermlistContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_function_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_stmt" ):
                return visitor.visitFunction_stmt(self)
            else:
                return visitor.visitChildren(self)




    def function_stmt(self):

        localctx = DE6Parser.Function_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(DE6Parser.ID)
            self.state = 152
            self.match(DE6Parser.LEFT_BRACKET)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 41875931654) != 0:
                self.state = 153
                self.termlist()


            self.state = 156
            self.match(DE6Parser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeletionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE_OPERATOR(self):
            return self.getToken(DE6Parser.DELETE_OPERATOR, 0)

        def lvalue(self):
            return self.getTypedRuleContext(DE6Parser.LvalueContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_deletion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeletion" ):
                return visitor.visitDeletion(self)
            else:
                return visitor.visitChildren(self)




    def deletion(self):

        localctx = DE6Parser.DeletionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_deletion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(DE6Parser.DELETE_OPERATOR)
            self.state = 159
            self.lvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EchoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ECHO(self):
            return self.getToken(DE6Parser.ECHO, 0)

        def value(self):
            return self.getTypedRuleContext(DE6Parser.ValueContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_echo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEcho" ):
                return visitor.visitEcho(self)
            else:
                return visitor.visitChildren(self)




    def echo(self):

        localctx = DE6Parser.EchoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_echo)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(DE6Parser.ECHO)
                self.state = 162
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(DE6Parser.ECHO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(DE6Parser.ConditionContext,0)


        def TEST_SYMBOL(self):
            return self.getToken(DE6Parser.TEST_SYMBOL, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DE6Parser.ActionContext)
            else:
                return self.getTypedRuleContext(DE6Parser.ActionContext,i)


        def TEST_SEPERATOR(self):
            return self.getToken(DE6Parser.TEST_SEPERATOR, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_conditional_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_statement" ):
                return visitor.visitConditional_statement(self)
            else:
                return visitor.visitChildren(self)




    def conditional_statement(self):

        localctx = DE6Parser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_conditional_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.condition()
            self.state = 167
            self.match(DE6Parser.TEST_SYMBOL)
            self.state = 168
            self.action()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 170
                self.match(DE6Parser.TEST_SEPERATOR)
                self.state = 171
                self.action()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DE6Parser.ValueContext)
            else:
                return self.getTypedRuleContext(DE6Parser.ValueContext,i)


        def conditionOperator(self):
            return self.getTypedRuleContext(DE6Parser.ConditionOperatorContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DE6Parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.value()
            self.state = 175
            self.conditionOperator()
            self.state = 176
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(DE6Parser.EQUALS, 0)

        def MATCHES(self):
            return self.getToken(DE6Parser.MATCHES, 0)

        def NOT_EQUALS(self):
            return self.getToken(DE6Parser.NOT_EQUALS, 0)

        def NOT_MATCHES(self):
            return self.getToken(DE6Parser.NOT_MATCHES, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_conditionOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionOperator" ):
                return visitor.visitConditionOperator(self)
            else:
                return visitor.visitChildren(self)




    def conditionOperator(self):

        localctx = DE6Parser.ConditionOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_conditionOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0):
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


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DE6Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(DE6Parser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(DE6Parser.ValueContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = DE6Parser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(DE6Parser.ID)
            self.state = 181
            self.match(DE6Parser.ASSIGN)
            self.state = 182
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DE6Parser.RULE_description

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DescribeHiddenVariableContext(DescriptionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.DescriptionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DESCRIBE(self):
            return self.getToken(DE6Parser.DESCRIBE, 0)
        def ID(self):
            return self.getToken(DE6Parser.ID, 0)
        def HIDDEN_TOKEN(self):
            return self.getToken(DE6Parser.HIDDEN_TOKEN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescribeHiddenVariable" ):
                return visitor.visitDescribeHiddenVariable(self)
            else:
                return visitor.visitChildren(self)


    class DescribeImmutableVariableContext(DescriptionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.DescriptionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DESCRIBE(self):
            return self.getToken(DE6Parser.DESCRIBE, 0)
        def ID(self):
            return self.getToken(DE6Parser.ID, 0)
        def IMMUTABLE_TOKEN(self):
            return self.getToken(DE6Parser.IMMUTABLE_TOKEN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescribeImmutableVariable" ):
                return visitor.visitDescribeImmutableVariable(self)
            else:
                return visitor.visitChildren(self)


    class DescribeConstantVariableContext(DescriptionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.DescriptionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DESCRIBE(self):
            return self.getToken(DE6Parser.DESCRIBE, 0)
        def ID(self):
            return self.getToken(DE6Parser.ID, 0)
        def CONST_TOKEN(self):
            return self.getToken(DE6Parser.CONST_TOKEN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescribeConstantVariable" ):
                return visitor.visitDescribeConstantVariable(self)
            else:
                return visitor.visitChildren(self)


    class DescribeNamedVariableContext(DescriptionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DE6Parser.DescriptionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DESCRIBE(self):
            return self.getToken(DE6Parser.DESCRIBE, 0)
        def ID(self):
            return self.getToken(DE6Parser.ID, 0)
        def STRING(self):
            return self.getToken(DE6Parser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescribeNamedVariable" ):
                return visitor.visitDescribeNamedVariable(self)
            else:
                return visitor.visitChildren(self)



    def description(self):

        localctx = DE6Parser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_description)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = DE6Parser.DescribeNamedVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(DE6Parser.DESCRIBE)
                self.state = 185
                self.match(DE6Parser.ID)
                self.state = 186
                self.match(DE6Parser.STRING)
                pass

            elif la_ == 2:
                localctx = DE6Parser.DescribeHiddenVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(DE6Parser.DESCRIBE)
                self.state = 188
                self.match(DE6Parser.ID)
                self.state = 189
                self.match(DE6Parser.HIDDEN_TOKEN)
                pass

            elif la_ == 3:
                localctx = DE6Parser.DescribeConstantVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(DE6Parser.DESCRIBE)
                self.state = 191
                self.match(DE6Parser.ID)
                self.state = 192
                self.match(DE6Parser.CONST_TOKEN)
                pass

            elif la_ == 4:
                localctx = DE6Parser.DescribeImmutableVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.match(DE6Parser.DESCRIBE)
                self.state = 194
                self.match(DE6Parser.ID)
                self.state = 195
                self.match(DE6Parser.IMMUTABLE_TOKEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Export_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT(self):
            return self.getToken(DE6Parser.EXPORT, 0)

        def ID(self):
            return self.getToken(DE6Parser.ID, 0)

        def STRING(self):
            return self.getToken(DE6Parser.STRING, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_export_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExport_stmt" ):
                return visitor.visitExport_stmt(self)
            else:
                return visitor.visitChildren(self)




    def export_stmt(self):

        localctx = DE6Parser.Export_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_export_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(DE6Parser.EXPORT)
            self.state = 199
            self.match(DE6Parser.ID)
            self.state = 200
            self.match(DE6Parser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveAllPrivateTagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE_ALL_PRIVATE_TAGS(self):
            return self.getToken(DE6Parser.REMOVE_ALL_PRIVATE_TAGS, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_removeAllPrivateTags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveAllPrivateTags" ):
                return visitor.visitRemoveAllPrivateTags(self)
            else:
                return visitor.visitChildren(self)




    def removeAllPrivateTags(self):

        localctx = DE6Parser.RemoveAllPrivateTagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_removeAllPrivateTags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(DE6Parser.REMOVE_ALL_PRIVATE_TAGS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION_WORD(self):
            return self.getToken(DE6Parser.VERSION_WORD, 0)

        def STRING(self):
            return self.getToken(DE6Parser.STRING, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_version

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion" ):
                return visitor.visitVersion(self)
            else:
                return visitor.visitChildren(self)




    def version(self):

        localctx = DE6Parser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(DE6Parser.VERSION_WORD)
            self.state = 205
            self.match(DE6Parser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def public_tag(self):
            return self.getTypedRuleContext(DE6Parser.Public_tagContext,0)


        def pvt_tag(self):
            return self.getTypedRuleContext(DE6Parser.Pvt_tagContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_tag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag" ):
                return visitor.visitTag(self)
            else:
                return visitor.visitChildren(self)




    def tag(self):

        localctx = DE6Parser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_tag)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.public_tag()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.pvt_tag()
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


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def public_tag(self):
            return self.getTypedRuleContext(DE6Parser.Public_tagContext,0)


        def pvt_tag(self):
            return self.getTypedRuleContext(DE6Parser.Pvt_tagContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = DE6Parser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_element)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.public_tag()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.pvt_tag()
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


    class Seq_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(DE6Parser.ElementContext,0)


        def itemnumber(self):
            return self.getTypedRuleContext(DE6Parser.ItemnumberContext,0)


        def seq_wildcard(self):
            return self.getTypedRuleContext(DE6Parser.Seq_wildcardContext,0)


        def getRuleIndex(self):
            return DE6Parser.RULE_seq_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq_element" ):
                return visitor.visitSeq_element(self)
            else:
                return visitor.visitChildren(self)




    def seq_element(self):

        localctx = DE6Parser.Seq_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_seq_element)
        self._la = 0 # Token type
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.element()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 216
                    self.itemnumber()


                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.seq_wildcard()
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


    class TagpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(DE6Parser.ElementContext,0)


        def seq_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DE6Parser.Seq_elementContext)
            else:
                return self.getTypedRuleContext(DE6Parser.Seq_elementContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(DE6Parser.SLASH)
            else:
                return self.getToken(DE6Parser.SLASH, i)

        def getRuleIndex(self):
            return DE6Parser.RULE_tagpath

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagpath" ):
                return visitor.visitTagpath(self)
            else:
                return visitor.visitChildren(self)




    def tagpath(self):

        localctx = DE6Parser.TagpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_tagpath)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 222
                    self.element()
                    pass

                elif la_ == 2:
                    self.state = 223
                    self.seq_element()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 226
                        self.seq_element()
                        self.state = 227
                        self.match(DE6Parser.SLASH)

                    else:
                        raise NoViableAltException(self)
                    self.state = 231 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 235
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 233
                    self.element()
                    pass

                elif la_ == 2:
                    self.state = 234
                    self.seq_element()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemnumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(DE6Parser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(DE6Parser.RIGHT_BRACKET, 0)

        def INTEGER(self):
            return self.getToken(DE6Parser.INTEGER, 0)

        def ITEM_WILDCARD(self):
            return self.getToken(DE6Parser.ITEM_WILDCARD, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_itemnumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemnumber" ):
                return visitor.visitItemnumber(self)
            else:
                return visitor.visitChildren(self)




    def itemnumber(self):

        localctx = DE6Parser.ItemnumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_itemnumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(DE6Parser.LEFT_BRACKET)
            self.state = 240
            _la = self._input.LA(1)
            if not(_la==8 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 241
            self.match(DE6Parser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seq_wildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEQ_WILDCARD(self):
            return self.getToken(DE6Parser.SEQ_WILDCARD, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_seq_wildcard

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq_wildcard" ):
                return visitor.visitSeq_wildcard(self)
            else:
                return visitor.visitChildren(self)




    def seq_wildcard(self):

        localctx = DE6Parser.Seq_wildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_seq_wildcard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(DE6Parser.SEQ_WILDCARD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Public_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC_GROUP(self):
            return self.getToken(DE6Parser.PUBLIC_GROUP, 0)

        def COMMA(self):
            return self.getToken(DE6Parser.COMMA, 0)

        def PUBLIC_ELEMENT(self):
            return self.getToken(DE6Parser.PUBLIC_ELEMENT, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_public_tag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPublic_tag" ):
                return visitor.visitPublic_tag(self)
            else:
                return visitor.visitChildren(self)




    def public_tag(self):

        localctx = DE6Parser.Public_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_public_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(DE6Parser.PUBLIC_GROUP)
            self.state = 246
            self.match(DE6Parser.COMMA)
            self.state = 247
            self.match(DE6Parser.PUBLIC_ELEMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pvt_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PVT_GROUP(self):
            return self.getToken(DE6Parser.PVT_GROUP, 0)

        def COMMA(self):
            return self.getToken(DE6Parser.COMMA, 0)

        def PVT_ELEMENT(self):
            return self.getToken(DE6Parser.PVT_ELEMENT, 0)

        def getRuleIndex(self):
            return DE6Parser.RULE_pvt_tag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPvt_tag" ):
                return visitor.visitPvt_tag(self)
            else:
                return visitor.visitChildren(self)




    def pvt_tag(self):

        localctx = DE6Parser.Pvt_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_pvt_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(DE6Parser.PVT_GROUP)
            self.state = 250
            self.match(DE6Parser.COMMA)
            self.state = 251
            self.match(DE6Parser.PVT_ELEMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





