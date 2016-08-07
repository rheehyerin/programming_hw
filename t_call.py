class Calculator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, x, y):
        print("called")
        self.base += (x+y) #results are getiing accumulated.
        return self.base
    '''
    def __call__(self, x, y):
        return x+y
    '''

calculator = Calculator(10)

print(calculator(1, 2)) #calculator.__call__(1, 2)
print(calculator(1, 2))
print(calculator(1, 2))
print(calculator(1, 2))