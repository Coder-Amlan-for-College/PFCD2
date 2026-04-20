class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    
    # += operator
    def __iadd__(self, other):
        self.r += other.r
        self.i += other.i
        return self
    
    # unary minus (-c)
    def __neg__(self):
        return Complex(-self.r, -self.i)
    
    # unary plus (+c)
    def __pos__(self):
        return Complex(+self.r, +self.i)
    
    # ~ operator (conjugate)
    def __invert__(self):
        return Complex(self.r, -self.i)
    
    def __str__(self):
        s = '+' if self.i >= 0 else '-'
        return f"{self.r}{s}{abs(self.i)}i"

c1 = Complex(2,3)
c2 = Complex(3,-3)

sum = c1+c2
print(c1,c2,sep="\n")
print(sum)
print(-c1)
c1 += c2
print(c1)