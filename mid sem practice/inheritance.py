'''8) Write a Python program that defines a base class Vehicle with 
attributes make and model, and a
method display info(). Create a subclass Car that inherits from 
Vehicle and adds an additional at
tribute num doors. Instantiate both Vehicle and Car objects, call 
their display info() methods, and
explain how the subclass inherits and extends the functionality of 
the base class.'''

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def display(self):
        print("Make:",self.make)
        print("Model:",self.model)
    
class Car(Vehicle):
    def __init__(self,make,model,doors):
        super().__init__(make,model)
        self.doors = doors
    
    def display(self):
        super().display()
        print("Doors:",self.doors)
    

car = Car("1","2",4)
car.display()
