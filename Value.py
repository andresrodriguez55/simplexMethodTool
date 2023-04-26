from NumericalOperations import NumericalOperations

class Value:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def __repr__(self):
        result = str(self.numerator)
        if(self.denominator != 1):
            result += '/' + str(self.denominator)
        return result

    def simplify(self):
        numericalOperations = NumericalOperations()
        gcd = numericalOperations.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd