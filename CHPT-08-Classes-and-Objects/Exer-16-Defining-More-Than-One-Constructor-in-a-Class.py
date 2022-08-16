# Exer-16-Defining-More-Than-One-Constructor-in-a-Class

import time

class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2012, 12, 21)  # Primary
b = Date.today()        # Alternate

###

class Date:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
            self.year, self.month, self.day = args

a = Date(2012, 12, 21)  # Clear. A specific date.
b = Date()              # ??? What does this do?

# Class method version
c = Date.today()        # Clear. Today's date.