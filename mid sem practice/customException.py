class InvalidAgeException(Exception):
    def __init__(self,msg):
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self):
        return f"{self.msg}"

try:
    age = -18
    if age<0:
        raise InvalidAgeException("Age Cannot be negative")

except InvalidAgeException as e:
    print(e)
        
