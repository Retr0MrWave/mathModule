from ..number_theory.GCDandLCM import gcd

class fraction:
    def __init__(self, n, d):
        if not(type(n) is int and type(d) is int):
	        raise TypeError("Numerator (n) and denominator (d) must both be integers")
        if d == 0:
            raise ZeroDivisionError
        self.n = n
        self.d = d
    
    def simplify(self):
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
    
    def getDecimal(self):
        return self.n/self.d