# Exer-12-Defining-an-Interface-or-Abstract-Base-Class

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

a = IStream()  # TypeError: Can't instantiate abstract class

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        ...
    def write(self, data):
        ...
        
