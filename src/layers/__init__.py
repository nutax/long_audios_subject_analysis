

class Layer:
    def __init__(self, *args):
        self.sublayers = {}
        for arg in args:
            if isinstance(arg, Layer):
                sublayer = type(arg).__name__
                self.sublayers[sublayer] = arg
                self.sublayers[sublayer].parent = self

    def call(self, sublayer, *args):
        if sublayer in self.sublayers:
            return self.sublayers[sublayer](*args)
        else:
            return self.parent.call(sublayer, *args)
