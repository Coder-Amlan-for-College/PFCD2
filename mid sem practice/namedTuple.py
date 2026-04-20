from collections import namedtuple

Student = namedtuple("Student",["name","age"])

s1 = Student("Amlan",18)
print(s1)
s1.age = 25
print(s1)