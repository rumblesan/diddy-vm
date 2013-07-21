#!/usr/bin/env python

import unittest
from lexer import lexer
from progdata import progdata


class Testlexer(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on lexer")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.lexer = lexer()

    def tearDown(self):
        del self.lexer

    def test_creation(self):
        self.assertIsInstance(self.lexer, lexer)

    def test_parse_float(self):
        input_data = progdata("44.67  ")
        number, prog_data = self.lexer.parse_number(input_data)
        self.assertEqual(number, ("NUMBER", 44.67))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_parse_int(self):
        input_data = progdata("4467  ")
        number, prog_data = self.lexer.parse_number(input_data)
        self.assertEqual(number, ("NUMBER", 4467))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_parse_name(self):
        input_data = progdata("name  ")
        name, prog_data = self.lexer.parse_name(input_data)
        self.assertEqual(name, ("NAME", "name"))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_parse_symbol(self):
        input_data = progdata("++  ")
        symbol, prog_data = self.lexer.parse_symbol(input_data)
        self.assertEqual(symbol, ("SYMBOL", "++"))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_parse_semicolon(self):
        input_data = progdata(""";  """)
        semicolon, prog_data = self.lexer.parse_semicolon(input_data)
        self.assertEqual(semicolon, ("SEMICOLON", ))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_parse_open_paren(self):
        input_data = progdata("(  ")
        paren, prog_data = self.lexer.parse_paren(input_data)
        self.assertEqual(paren, ("OPENPAREN", ))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_parse_close_paren(self):
        input_data = progdata(")  ")
        paren, prog_data = self.lexer.parse_paren(input_data)
        self.assertEqual(paren, ("CLOSEPAREN", ))
        self.assertEqual(prog_data.remaining(), "  ")

    def test_basic_parse(self):
        input_data = """
        var foo = 45 + 5.4;
        var bar = foo - 2;
        """
        expected_output = [
            ("ASSIGNMENT", ),
            ("NAME", "foo"),
            ("SYMBOL", "="),
            ("NUMBER", 45),
            ("SYMBOL", "+"),
            ("NUMBER", 5.4),
            ("SEMICOLON", ),
            ("ASSIGNMENT", ),
            ("NAME", "bar"),
            ("SYMBOL", "="),
            ("NAME", "foo"),
            ("SYMBOL", "-"),
            ("NUMBER", 2),
            ("SEMICOLON", ),
            ("EOF", )
        ]
        p = progdata(input_data)
        tokens = self.lexer.parse(p)
        self.assertEqual(tokens, expected_output)

    def test_more_complex_parse(self):
        input_data = """
        def foo(one, two) {
            var bacon = one + 2;
            return bacon * (2 + two);
        }
        var bar = foo(2.3, 8);
        """
        expected_output = [
            ("FUNCTIONDEF", ),
            ("NAME", "foo"),
            ("OPENPAREN", ),
            ("NAME", "one"),
            ("SYMBOL", ","),
            ("NAME", "two"),
            ("CLOSEPAREN", ),
            ("OPENBRACKET", ),
            ("ASSIGNMENT", ),
            ("NAME", "bacon"),
            ("SYMBOL", "="),
            ("NAME", "one"),
            ("SYMBOL", "+"),
            ("NUMBER", 2),
            ("SEMICOLON", ),
            ("FUNCTIONRETURN", ),
            ("NAME", "bacon"),
            ("SYMBOL", "*"),
            ("OPENPAREN", ),
            ("NUMBER", 2),
            ("SYMBOL", "+"),
            ("NAME", "two"),
            ("CLOSEPAREN", ),
            ("SEMICOLON", ),
            ("CLOSEBRACKET", ),
            ("ASSIGNMENT", ),
            ("NAME", "bar"),
            ("SYMBOL", "="),
            ("NAME", "foo"),
            ("OPENPAREN", ),
            ("NUMBER", 2.3),
            ("SYMBOL", ","),
            ("NUMBER", 8),
            ("CLOSEPAREN", ),
            ("SEMICOLON", ),
            ("EOF", )
        ]
        p = progdata(input_data)
        tokens = self.lexer.parse(p)
        self.assertEqual(tokens, expected_output)
