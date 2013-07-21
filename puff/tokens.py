#!/usr/bin/env python


def NUMBER(value):
    return ("NUMBER", value)


def NAME(value):
    return ("NAME", value)


def SYMBOL(value):
    return ("SYMBOL", value)


def SEMICOLON():
    return ("SEMICOLON", )


def OPENPAREN():
    return ("OPENPAREN", )


def CLOSEPAREN():
    return ("CLOSEPAREN", )


def OPENBRACKET():
    return ("OPENBRACKET", )


def CLOSEBRACKET():
    return ("CLOSEBRACKET", )


def ASSIGNMENT():
    return ("ASSIGNMENT", )


def EOF():
    return ("EOF", )


def FUNCTIONDEF():
    return ("FUNCTIONDEF", )


def FUNCTIONRETURN():
    return ("FUNCTIONRETURN", )
