from ..number_theory.GCDandLCM import gcd, lcm

class fraction:
    def __init__(self, n, d):
        if not((type(n) is int or type(n) is fraction) and (type(d) is int or type(d) is fraction)):
	        raise TypeError("Numerator (n) and denominator (d) must both be integers")
        if d == 0:
            raise ZeroDivisionError
        self.d = 1
        if type(n) is int:
            self.n = n
        else:
            self.n = n.n
            self.d = n.d
        if type(d) is int:
            self.d *= d
        else:
            self.n *= d.d
            self.d *= d.n
    
    def simplify(self):
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
    
    def getDecimal(self):
        return self.n/self.d
    
    def __add__(self, other):
        r = fraction(self.n * other.d + other.n * self.d, self.d*other.d)
        r.simplify()
        return r
    
    def __sub__(self, other):
        r = fraction(self.n * other.d - other.n * self.d, self.d*other.d)
        r.simplify()
        return r
    
    def __mul__(self, other):
        r = fraction(self.n * other.n, self.d * other.d)
        r.simplify()
        return r

    def __truediv__(self, other):
        r = fraction(self.n * other.d, self.d * other.n)
        r.simplify()
        return r

    def __eq__(self, other):
        selfs = self
        selfs.simplify()
        others = other
        others.simplify()
        return selfs.n == others.n and selfs.d == others.d

    def __ne__(self, other):
        selfs = self
        selfs.simplify()
        others = other
        others.simplify()
        return selfs.n != others.n or selfs.d != others.d
    
    def __lt__(self, other):
        selfs = self
        selfs.simplify()
        others = other
        others.simplify()
        return selfs.n * others.d < others.n * selfs.d
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not(self <= other)
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __iadd__(self, other):
        self = self + other
    
    def __isub__(self, other):
        self = self - other
    
    def __imul__(self, other):
        self = self * other
    
    def __idiv__(self, other):
        self = self / other
    
    def __str__(self):
        return self.n + "/" + self.d