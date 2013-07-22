

class addition(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class subtract(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class product(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class division(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class greater(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class less(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class equal(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right





class expression(object):

    def __init__(self, symbols):
        self.symbols = symbols


class assignment(object):

    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class func_def(object):

    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body


class func_call(object):

    def __init__(self, name, args):
        self.name = name
        self.args = args
