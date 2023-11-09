from src.layers import Layer

class A (Layer):
    def __call__(self):
        print(self.call('B', 3) + self.call('C'))

class B (Layer):
    def __call__(self, n):
        return 1 + n

class C (Layer):
    def __call__(self):
        return self.call('B', 1) + 1



A(B(), C())()


from src.layers.ExperimentLayer import ExperimentLayer
from src.layers.ResearchLayer import ResearchLayer