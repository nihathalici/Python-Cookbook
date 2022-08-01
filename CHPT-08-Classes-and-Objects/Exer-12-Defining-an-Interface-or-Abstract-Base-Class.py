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

###

def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')

###

import io

IStream.register(io.IOBase)

f = open('foo.txt')
isinstance(f, IStream)

###

from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass

###

import collections

if isinstance(x, collections.Sequence):
    ...

if isinstance(x, collections.Iterable):
    ...

if isinstance(x, collections.Sized):
    ...

if isinstance(x, collections.Mapping):
    ...

from decimal import Decimal
import numbers

x = Decimal('3.4')
isinstance(x, numbers.Real)
    
