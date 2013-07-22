#!/usr/bin/env python

import re
import tokens as t


class lexer(object):

    def __init__(self):

        self.num_re = re.compile("""[0-9]""")
        self.name_re = re.compile("""[a-zA-Z]""")
        self.symb_re = re.compile("""[+\-*/%<>&=,]""")

    def parse(self, prog_data):
        while True:
            val = prog_data.peek()
            if val == " " or val == "\t":
                prog_data.pop()
            elif val == "\n":
                prog_data.pop()
            elif self.num_re.match(val):
                prog_data.add_token(self.parse_number(prog_data))
            elif self.name_re.match(val):
                prog_data.add_token(self.parse_name(prog_data))
            elif self.symb_re.match(val):
                prog_data.add_token(self.parse_symbol(prog_data))
            elif val == ";":
                prog_data.add_token(self.parse_semicolon(prog_data))
            elif val is "(" or val is ")":
                prog_data.add_token(self.parse_paren(prog_data))
            elif val is "{" or val is "}":
                prog_data.add_token(self.parse_bracket(prog_data))
            else:
                print("unexpected", val)
                prog_data.pop()

            if prog_data.finished():
                prog_data.add_token(t.EOF())
                return prog_data.tokens

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
                break
        return t.NUMBER(float(number))

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
        return token

    def parse_symbol(self, prog_data):
        symbol = ''
        while True:
            val = prog_data.peek()
            if self.symb_re.match(val):
                symbol += prog_data.pop()
            else:
                break
        return t.SYMBOL(symbol)

    def parse_semicolon(self, prog_data):
        prog_data.pop()
        return t.SEMICOLON()

    def parse_paren(self, prog_data):
        val = prog_data.pop()
        if val == "(":
            p = t.OPENPAREN()
        elif val == ")":
            p = t.CLOSEPAREN()
        return p

    def parse_bracket(self, prog_data):
        val = prog_data.pop()
        if val == "{":
            p = t.OPENBRACKET()
        elif val == "}":
            p = t.CLOSEBRACKET()
        return p


if __name__ == '__main__':
    import unittest
    from tests.testlexer import Testlexer
    Testlexer.header()
    unittest.main()
