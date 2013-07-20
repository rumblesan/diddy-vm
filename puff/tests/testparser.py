#!/usr/bin/env python

import unittest
from lexer import lexer
from parser import parser
from progdata import progdata

from ast import assignment, func_def


class Testparser(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on parser")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.parser = parser()
        self.lexer = lexer()

    def tearDown(self):
        del self.parser
        del self.lexer

    def test_creation(self):
        self.assertIsInstance(self.parser, parser)

    def test_basic_assignment(self):
        program = "var foo = 2;"
        p = progdata(program)
        tokens = self.lexer.parse(p)
        ast = self.parser.parse(tokens)
        self.assertIsInstance(ast[0], assignment)

    def test_bigger_program(self):
        program = """
        var foo = 2;
        var bar = foo + 3;
        def bam(a) {
            return a + 2;
        }
        var bim = bam(bar);
        """
        p = progdata(program)
        tokens = self.lexer.parse(p)
        ast = self.parser.parse(tokens)
        self.assertIsInstance(ast[0], assignment)
        self.assertIsInstance(ast[1], assignment)
        self.assertIsInstance(ast[2], func_def)
        self.assertIsInstance(ast[3], assignment)
