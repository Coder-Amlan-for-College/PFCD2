from dataclasses import dataclass

class InvalidAge(Exception):
    def __init__(self,msg):
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self):
        return f"{self.msg}"


@dataclass
class Student:
    name : str
    age :  int

    def checkAge(self):
        if self.age<0:
            raise InvalidAge("AGE CANNOT BE NEGATIVE")

s1 = Student("Amlan",18)
try:
    s1 = Student("Amlan",-18)
    s1.checkAge()
    print(s1)
    
except InvalidAge as e:
    print(e)
