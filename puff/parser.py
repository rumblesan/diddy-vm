#!/usr/bin/env python

from ast import func_def, assignment

from progdata import progdata


class parser(object):

    def __init__(self):
        pass

    def parse(self, program):
        program_data = progdata(program)
        blocks = []
        p = True
        while p:
            e = self.parse_line(program_data)
            if not e:
                break
            blocks.append(e)

        return blocks

    def parse_line(self, program_data):
        e = None
        t = program_data.peek()

        if t[0] == "EOF":
            e = None
        elif t[0] == "NAME":
            e = self.parse_line(program_data)
        elif t[0] == "FUNCTIONDEF":
            e = self.parse_function(program_data)
        elif t[0] == "ASSIGNMENT":
            e = self.parse_assignment(program_data)
        elif t[0] == "FUNCTIONRETURN":
            e = self.parse_function_return(program_data)
        else:
            raise SyntaxError("Not expecting " + t[0])

        return e

    def parse_expression(self, program_data):
        expr = []
        while True:
            e = program_data.pop()
            if e[0] == "SEMICOLON":
                break
            else:
                expr.append(e)

        for s in expr:
            #This is where precedence ordering will occour
            pass
        return expr

    def parse_assignment(self, program_data):
        v = program_data.pop()
        if v[0] != "ASSIGNMENT":
            raise SyntaxError("Expecting 'var not '%s'" % v[1])
        var_name = program_data.pop()
        eq = program_data.pop()
        if eq[1] != "=":
            raise SyntaxError("Expecting '=' not '%s'" % eq[1])
        var_expr = self.parse_expression(program_data)

        return assignment(var_name, var_expr)

    def parse_function(self, program_data):
        d = program_data.pop()
        if d[0] != "FUNCTIONDEF":
            raise SyntaxError("Expecting 'def' not '%s'" % d[1])
        func_name = program_data.pop()
        func_args = self.parse_function_args(program_data)

        func_body = self.parse_function_body(program_data)

        return func_def(func_name, func_args, func_body)

    def parse_function_args(self, program_data):
        if program_data.pop()[0] != "OPENPAREN":
            raise SyntaxError("Expecting '('")
        args = []
        expecting = "arg"
        p = True
        while p:
            arg = program_data.pop()
            if arg[0] == "NAME":
                if expecting == "comma":
                    raise SyntaxError("Expecting ',' or ')'")
                args.append(arg)
                expecting = "comma"
            elif arg[0] == "CLOSEPAREN":
                if expecting == "arg":
                    raise SyntaxError("Expecting argument")
                break
            elif arg[1] == ",":
                if expecting == "arg":
                    raise SyntaxError("Expecting argument or ')'")
                expecting = "arg"
        return args

    def parse_function_body(self, program_data):
        if program_data.pop()[0] != "OPENBRACKET":
            raise SyntaxError("Expecting '{'")
        exprs = []
        p = True
        while p:
            d = program_data.peek()
            if d[0] == "CLOSEBRACKET":
                program_data.pop()
                break
            else:
                exprs.append(self.parse_line(program_data))
        return exprs

    def parse_function_return(self, program_data):
        v = program_data.pop()
        if v[0] != "FUNCTIONRETURN":
            raise SyntaxError("Expecting 'return' not '%s'" % v[1])
        var_expr = self.parse_expression(program_data)
        return var_expr

    def parse_function_call(self, program_data):
        pass


if __name__ == '__main__':
    import unittest
    from tests.testparser import Testparser
    Testparser.header()
    unittest.main()
