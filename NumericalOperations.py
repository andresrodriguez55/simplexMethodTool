class NumericalOperations:
    def __init__(self):
        pass

    def __helperGcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a % b)
        
    def gcd(self, a, b):
        a = abs(a)
        b = abs(b)
        
        if a <= b:
            a, b = b, a
        return self.__helperGcd(a, b)
        