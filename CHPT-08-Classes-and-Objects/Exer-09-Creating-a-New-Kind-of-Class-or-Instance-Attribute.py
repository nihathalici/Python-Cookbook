# Exer-09-Creating-a-New-Kind-of-Class-or-Instance-Attribute

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)  # Calls Point.x.__get__(p,Point)
p.y = 5  # Calls Point.y.__set__(p, 5)
p.x = 2.3  # Calls Point.x.__set__(p, 2.3), raise TypeError      

###

# Does NOT work
class Point:
    def __init__(self, x, y):
        self.x = Integer('x')  # No! Must be a class variable
        self.y = Integer('y')
        self.x = x
        self.y = y

###

# Descriptor attribute for an integer type-checked attribute
class Integer:
    ...
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    ...

p = Point(2, 3)
p.x  # Calls Point.x.__get__(p, Point)
Point.x  # Calls Point.x.__get__(None, Point)

###

# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

    # Class decorator that applies it to selected attributes
    def typeassert(**kwargs):
        def decorate(cls):
            for name, expected_type in kwargs.items():
                setattr(cls, name, Typed(name, expected_type))
            return cls
        return decorate

    # Example use
    @typeassert(name=str, shares=int, price=float)
    class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
            
    
                
        
        
        


        


    
