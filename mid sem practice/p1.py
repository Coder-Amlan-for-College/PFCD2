class InvalidTimeException(Exception):
    def __init__(self,msg):
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self):
        return f"{self.msg}"

class Time:
    def __init__(self,hh,mm,ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    
    def isValid(self):
        h = int(self.hh)
        m = int(self.mm)
        s = int(self.ss)
        if h<0 or h>23:
            raise InvalidTimeException("Invalid Time")
        if m<0 or m>59:
            raise InvalidTimeException("Invalid Time")
        if s<0 or s>59:
            raise InvalidTimeException("Invalid Time")
    
    def convert(self):
        self.isValid()
        h = int(self.hh)
        m = int(self.mm)
        s = int(self.ss)

        period = "AM"
        if(h>=12):
            period="PM"
            if(h>12):
                h -= 12
        else:
            if h==0:
                h = 12
        
        print(f"{h:02d}:{m:02d}:{s:02d} {period}")
        
time = "25:05:07"
lst = time.split(":")
try:
    t1 = Time(lst[0],lst[1],lst[2])
    t1.convert()

except InvalidTimeException as e:
    print(e)
