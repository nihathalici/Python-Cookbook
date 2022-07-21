# Exer-04-Saving-Memory-When-Creating-a-Large-Number-of-Instances

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
