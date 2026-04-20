import math
class Shape:
    def area(self):
        print("Area")

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print(f"Area of circle is {(math.pi*self.r*self.r):.03f}")
    
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(f"Area of circle is {self.l*self.b:.02f}")


c1 = Circle(2)
r1 = Rectangle(2,3)
c1.area()
r1.area()