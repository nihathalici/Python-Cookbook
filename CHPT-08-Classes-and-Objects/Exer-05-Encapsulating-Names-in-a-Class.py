# Exer-05-Encapsulating-Names-in-a-Class

class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        ...

    def _internal_method(self):
        ...

class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        ...
    def public_method(self):
        ...
        self.__private_method()
        ...

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private
    # Does not override B.__private_method()
    def __private_method(self):
        ...

lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword


    
