#!/usr/bin/env python


class progdata(object):

    def __init__(self, program):
        self.program = program
        self.length = len(self.program)
        self.count = 0
        self.fin = False

        self.tokens = []

    def peek(self):
        if self.count >= self.length:
            return None
        else:
            return self.program[self.count]

    def pop(self):
        if self.count >= self.length:
            return None
        else:
            var = self.program[self.count]
            self.count += 1
            if self.count >= self.length:
                self.fin = True
            return var

    def unpop(self, count=1):
        if (self.count - count) <= 0:
            self.count = 0
        else:
            self.count -= count

    def finished(self):
        return self.fin

    def position(self):
        return self.count

    def remaining(self):
        if self.count >= self.length:
            return []
        else:
            return self.program[self.count:]

    def add_token(self, token):
        self.tokens.append(token)


if __name__ == '__main__':
    import unittest
    from tests.testprogdata import Testprogdata
    Testprogdata.header()
    unittest.main()
