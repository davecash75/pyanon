# Generated from DE6Parser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DE6Parser import DE6Parser
else:
    from DE6Parser import DE6Parser

# This class defines a complete generic visitor for a parse tree produced by DE6Parser.

class DE6ParserVisitor(ParseTreeVisitor):

    def __init__(self):
        super().__init__()
        self.statement_list = None
        self.version_string = None

    # Visit a parse tree produced by DE6Parser#script.
    def visitScript(self, ctx:DE6Parser.ScriptContext):
        self.statement_list = []
        n = ctx.getChildCount()
        for i in range(n):
            c = ctx.getChild(i)
            childResult = c.accept(self)
            if childResult is not None:
                self.statement_list.append(childResult)
        return self.statement_list

    # Visit a parse tree produced by DE6Parser#separator.
    def visitSeparator(self, ctx:DE6Parser.SeparatorContext):
        return None


    # Visit a parse tree produced by DE6Parser#statement.
    def visitStatement(self, ctx:DE6Parser.StatementContext):
        statements = self.visitChildren(ctx)
        return statements


    # Visit a parse tree produced by DE6Parser#action.
    def visitAction(self, ctx:DE6Parser.ActionContext):
        children = self.visitChildren(ctx)
        return {'Command': 'Action', 'children': children}


    # Visit a parse tree produced by DE6Parser#assign_if_exists.
    def visitAssign_if_exists(self, ctx:DE6Parser.Assign_if_existsContext):
        assignment={'Action':'Assignment_if_exists',
                   'Lvalue': self.visit(ctx.lvalue()),
                   'RValue': self.visit(ctx.value())
                   }
        return assignment


    # Visit a parse tree produced by DE6Parser#assignment.
    def visitAssignment(self, ctx:DE6Parser.AssignmentContext):
        assignment={'Action':'Assignment',
                   'Lvalue': self.visit(ctx.lvalue()),
                   'RValue': self.visit(ctx.value())
                   }
        return assignment


    # Visit a parse tree produced by DE6Parser#tagpathLvalue.
    def visitTagpathLvalue(self, ctx:DE6Parser.TagpathLvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#value.
    def visitValue(self, ctx:DE6Parser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DE6Parser#numberTerm.
    def visitNumberTerm(self, ctx:DE6Parser.NumberTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#stringTerm.
    def visitStringTerm(self, ctx:DE6Parser.StringTermContext):
        return {'Type': 'string', 'TermVal': ctx.STRING().getText()}

    # Visit a parse tree produced by DE6Parser#tagPathTerm.
    def visitTagPathTerm(self, ctx:DE6Parser.TagPathTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#functionTerm.
    def visitFunctionTerm(self, ctx:DE6Parser.FunctionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#idTerm.
    def visitIdTerm(self, ctx:DE6Parser.IdTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#variable.
    def visitVariable(self, ctx:DE6Parser.VariableContext):
        var_name = {
            'Type': 'Variable',
            'TermValue': ctx.ID().getText()
        }
        return var_name


    # Visit a parse tree produced by DE6Parser#intvalue.
    def visitIntvalue(self, ctx:DE6Parser.IntvalueContext):
        return {'Type': 'string', 'TermVal': ctx.INTEGER()}


    # Visit a parse tree produced by DE6Parser#floatvalue.
    def visitFloatvalue(self, ctx:DE6Parser.FloatvalueContext):
        return {'Type': 'string', 'TermVal': ctx.FLOAT()}


    # Visit a parse tree produced by DE6Parser#termlist.
    def visitTermlist(self, ctx:DE6Parser.TermlistContext):
        term_list = []
        for term in ctx.term():
            term_list.append(self.visit(term))
        return term_list

    # Visit a parse tree produced by DE6Parser#method.
    def visitMethod(self, ctx:DE6Parser.MethodContext):
        meth_statement = {
            'Type': 'method',
            'FunctionName': ctx.ID().getText(),
            'ArgList': self.visit(ctx.termlist()),
            'Text': ctx.getText(),
        }
        return meth_statement


    # Visit a parse tree produced by DE6Parser#function_stmt.
    def visitFunction_stmt(self, ctx:DE6Parser.Function_stmtContext):
        fn_statement = {
            'Type': 'function',
            'FunctionName': ctx.ID().getText(),
            'ArgList': self.visit(ctx.termlist()),
            'Text': ctx.getText(),
        }
        return fn_statement


    # Visit a parse tree produced by DE6Parser#deletion.
    def visitDeletion(self, ctx:DE6Parser.DeletionContext):
        print("Deleting")
        deletion = {'Action': 'Deletion',
                   'Lvalue': self.visit(ctx.lvalue()),
                   }
        return deletion


    # Visit a parse tree produced by DE6Parser#echo.
    def visitEcho(self, ctx:DE6Parser.EchoContext):
        print("Echo")
        echo_cmd = {
            'Action': 'Echo',
            'TermVal': self.visit(ctx.value())
        }
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#conditional_statement.
    def visitConditional_statement(self, ctx:DE6Parser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#condition.
    def visitCondition(self, ctx:DE6Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#conditionOperator.
    def visitConditionOperator(self, ctx:DE6Parser.ConditionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#initialization.
    def visitInitialization(self, ctx:DE6Parser.InitializationContext):
        init_var = {'Action': 'Initialization',
                'Variable': ctx.ID().getText(),
                'Value': self.visit(ctx.value()),
                }
        return init_var


    # Visit a parse tree produced by DE6Parser#describeNamedVariable.
    def visitDescribeNamedVariable(self, ctx:DE6Parser.DescribeNamedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#describeHiddenVariable.
    def visitDescribeHiddenVariable(self, ctx:DE6Parser.DescribeHiddenVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#describeConstantVariable.
    def visitDescribeConstantVariable(self, ctx:DE6Parser.DescribeConstantVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#describeImmutableVariable.
    def visitDescribeImmutableVariable(self, ctx:DE6Parser.DescribeImmutableVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#export_stmt.
    def visitExport_stmt(self, ctx:DE6Parser.Export_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#removeAllPrivateTags.
    def visitRemoveAllPrivateTags(self, ctx:DE6Parser.RemoveAllPrivateTagsContext):
        cmd = {'Command': 'RemoveAllPrivateTags'}
        return cmd


    # Visit a parse tree produced by DE6Parser#version.
    def visitVersion(self, ctx:DE6Parser.VersionContext):
        self.version = ctx.STRING().getText()
        return None


    # Visit a parse tree produced by DE6Parser#tag.
    def visitTag(self, ctx:DE6Parser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#element.
    def visitElement(self, ctx:DE6Parser.ElementContext):
        element = self.visitChildren(ctx)
        print(f"Found element {element=}")
        return element


    # Visit a parse tree produced by DE6Parser#seq_element.
    def visitSeq_element(self, ctx:DE6Parser.Seq_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#tagpath.
    def visitTagpath(self, ctx:DE6Parser.TagpathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#itemnumber.
    def visitItemnumber(self, ctx:DE6Parser.ItemnumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#seq_wildcard.
    def visitSeq_wildcard(self, ctx:DE6Parser.Seq_wildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DE6Parser#public_tag.
    def visitPublic_tag(self, ctx:DE6Parser.Public_tagContext):
        current_object = {
            'Type': 'DicomTag',
            'dcm_group': int(ctx.PUBLIC_GROUP().getText().strip("("),base=16),
            'dcm_element': int(ctx.PUBLIC_ELEMENT().getText().rstrip(")"),base=16),
        }
        return current_object


    # Visit a parse tree produced by DE6Parser#pvt_tag.
    def visitPvt_tag(self, ctx:DE6Parser.Pvt_tagContext):
        current_object = {
            'Type': "DicomTag",
            'dcm_group': int(ctx.PVT_GROUP().getText().strip("("),base=16),
            'dcm_element': int(ctx.PVT_ELEMENT().getText().rstrip(")"),base=16),
        }
        return current_object



del DE6Parser
