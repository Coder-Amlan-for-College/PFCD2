
class Student:
    def __init__(self,__name,__age):
        self.__name = __name
        self.__age = __age
    
    @property
    def age(self):
        return self.__age
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
    
    @age.setter
    def age(self,age):
        self.__age = age




s1 = Student("A",18)
print(s1.age)
print(s1.name)

s1.age = 22
s1.name = "Akash"
print(s1.age)
print(s1.name)

