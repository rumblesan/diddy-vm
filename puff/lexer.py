#!/usr/bin/env python

import re
import tokens as t


class lexer(object):

    def __init__(self):

        self.num_re = re.compile("""[0-9]""")
        self.name_re = re.compile("""[a-zA-Z]""")
        self.symb_re = re.compile("""[+\-*/%<>&=,]""")

    def parse_number(self, prog_data):
        number = ''
        is_float = False
        while True:
            val = prog_data.peek()
            if self.num_re.match(val):
                number += prog_data.pop()
            elif val is '.' and not is_float:
                number += prog_data.pop()
                is_float = True
            else:
                return (t.NUMBER(float(number)), prog_data)

    def parse_name(self, prog_data):
        name = ''
        token = None
        while True:
            val = prog_data.peek()
            if self.name_re.match(val):
                name += prog_data.pop()
            else:
                break
        if name == "def":
            token = t.FUNCTIONDEF()
        elif name == "var":
            token = t.ASSIGNMENT()
        elif name == "return":
            token = t.FUNCTIONRETURN()
        else:
            token = t.NAME(name)
        return (token, prog_data)

    def parse_symbol(self, prog_data):
        symbol = ''
        while True:
            val = prog_data.peek()
            if self.symb_re.match(val):
                symbol += prog_data.pop()
            else:
                return (t.SYMBOL(symbol), prog_data)

    def parse_semicolon(self, prog_data):
        val = prog_data.pop()
        if val == ";":
            return (t.SEMICOLON(), prog_data)
        else:
            message = "problem parsing semicolon, found '%s'" % val
            raise SyntaxError(message)

    def parse_paren(self, prog_data):
        val = prog_data.pop()
        if val == "(":
            return (t.OPENPAREN(), prog_data)
        elif val == ")":
            return (t.CLOSEPAREN(), prog_data)
        else:
            message = "problem parsing paren, found '%s'" % val
            raise SyntaxError(message)

    def parse_bracket(self, prog_data):
        val = prog_data.pop()
        if val == "{":
            return (t.OPENBRACKET(), prog_data)
        elif val == "}":
            return (t.CLOSEBRACKET(), prog_data)
        else:
            message = "problem parsing bracket, found '%s'" % val
            raise SyntaxError(message)

    def parse(self, prog_data):
        tokens = []
        while True:
            val = prog_data.peek()
            if val is ' ' or val == "\n":
                prog_data.pop()
            elif self.num_re.match(val):
                token, prog = self.parse_number(prog_data)
                tokens.append(token)
            elif self.name_re.match(val):
                token, prog = self.parse_name(prog_data)
                tokens.append(token)
            elif self.symb_re.match(val):
                token, prog = self.parse_symbol(prog_data)
                tokens.append(token)
            elif val == ";":
                token, prog = self.parse_semicolon(prog_data)
                tokens.append(token)
            elif val is "(" or val is ")":
                token, prog = self.parse_paren(prog_data)
                tokens.append(token)
            elif val is "{" or val is "}":
                token, prog = self.parse_bracket(prog_data)
                tokens.append(token)
            else:
                print("unexpected", val)
                prog_data.pop()

            if prog_data.finished():
                tokens.append(t.EOF())
                return tokens


if __name__ == '__main__':
    import unittest
    from tests.testlexer import Testlexer
    Testlexer.header()
    unittest.main()
