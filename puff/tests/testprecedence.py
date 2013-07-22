#!/usr/bin/env python

import unittest
from precedence import precedence
import tokens as t


class Testprecedence(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on precedence")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.precedence = precedence()

    def tearDown(self):
        del self.precedence

    def test_creation(self):
        self.assertIsInstance(self.precedence, precedence)

    def test_simple(self):
        input_program = [t.NUMBER(4), t.SYMBOL("+"), t.NUMBER(3)]
        expected_output = [t.NUMBER(4), t.NUMBER(3), t.SYMBOL("+")]
        parse_output = self.precedence.parse(input_program)
        self.assertEqual(parse_output, expected_output)

    def test_more_complex(self):
        input_program = [t.NUMBER(4), t.SYMBOL("+"), t.NUMBER(3), t.SYMBOL("*"), t.NUMBER(5)]
        expected_output = [t.NUMBER(4), t.NUMBER(3), t.NUMBER(5), t.SYMBOL("*"), t.SYMBOL("+")]
        parse_output = self.precedence.parse(input_program)
        self.assertEqual(parse_output, expected_output)

    def test_parens(self):
        input_program = [t.OPENPAREN(), t.NUMBER(4), t.SYMBOL("+"), t.NUMBER(3), t.CLOSEPAREN(),  t.SYMBOL("*"), t.NUMBER(5)]
        expected_output = [t.NUMBER(4), t.NUMBER(3), t.SYMBOL("+"), t.NUMBER(5), t.SYMBOL("*")]
        parse_output = self.precedence.parse(input_program)
        self.assertEqual(parse_output, expected_output)

    def test_complex(self):
        input_program = [t.OPENPAREN(), t.NUMBER(4), t.SYMBOL("+"), t.NUMBER(3), t.CLOSEPAREN(),  t.SYMBOL("*"), t.NUMBER(5)]
        expected_output = [t.NUMBER(4), t.NUMBER(3), t.SYMBOL("+"), t.NUMBER(5), t.SYMBOL("*")]
        parse_output = self.precedence.parse(input_program)
        self.assertEqual(parse_output, expected_output)


