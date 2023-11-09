class Layer:
    def __init__(self, *args):
        self.sublayers = {}
        for arg in args:
            if isinstance(arg, Layer):
                sublayer = type(arg).__name__
                self.sublayers[sublayer] = arg
                self.sublayers[sublayer].parent = self

    def call(self, sublayer, *args):
        if self.sublayers[sublayer] is None:
            return self.parent.call(sublayer, *args)
        else:
            return self.sublayers[sublayer](*args)

class A (Layer):
    def __call__(self):
        print(self.call('b', 3) + self.call('c'))

class B (Layer):
    def __call__(self, n):
        return 1 + n

class C (Layer):
    def __call__(self):
        return self.call('b', 1) + 1



A(B(), C())()

