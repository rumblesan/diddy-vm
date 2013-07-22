#!/usr/bin/env python


class precedence(object):

    def __init__(self):
        p = {}
        p['('] = 1000
        p['*'] = 1
        p['/'] = 2
        p['+'] = 3
        p['-'] = 4
        p['='] = 5
        p['<'] = 5
        p['>'] = 5
        self.p = p

        self.ops_stack = []
        self.output_queue = []

    def parse(self, symbols):
        self.ops_stack = []
        self.output_queue = []

        for s in symbols:
            if s[0] == "SYMBOL":
                if not self.ops_stack:
                    self.ops_stack.append(s)
                else:
                    if self.get_precedence(s) > self.get_precedence(self.ops_stack[0]):
                        self.output_queue.append(self.ops_stack.pop(0))
                    self.ops_stack.append(s)
            elif s[0] == "OPENPAREN":
                self.ops_stack.append(s)
            elif s[0] == "CLOSEPAREN":
                while True:
                    top_sym = self.ops_stack.pop()
                    if top_sym[0] == "OPENPAREN":
                        break
                    else:
                        self.output_queue.append(top_sym)
            else:
                self.output_queue.append(s)
        self.ops_stack.reverse()
        return self.output_queue + self.ops_stack

    def get_precedence(self, symbol):
        p = -1
        if symbol[0] == "SYMBOL":
            p = self.p[symbol[1]]
        elif symbol[0] == "OPENPAREN":
            p = self.p["("]
        return p



if __name__ == '__main__':
    import unittest
    from tests.testprecedence import Testprecedence
    Testprecedence.header()
    unittest.main()
