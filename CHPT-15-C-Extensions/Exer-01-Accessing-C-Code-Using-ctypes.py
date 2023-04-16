# Exer-01-Accessing-C-Code-Using-ctypes

/* sample.c */_method
#include <math.h>

/* Compute the greatest common divisor */
int gcd(int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}

/* Test if (x0, y0) is in the Mandelbrot set or not */
int in_mandel(double x0, double y0, int n) {
    double x = 0, y = 0, xtemp;
    while (n > 0) {
      xtemp = x*x - y*y + x0;
      y = 2*x*y + y0;
      x = xtemp;
      n -= 1;
      if (x*x + y*y > 4) return 0;
    }
    return 1;
}

/* Divide two numbers */
int divide(int a, int b, int *remainder) {
    int quot = a / b;
    *remainder = a % b;
    return quot;
}

/* Average values in an array */
double avg(double *a, int n) {
    int i;
    double total = 0.0;
    for (i = 0; i < n; i++) {
      total += a[i];
    }
    return total / n;
}

/* A C data structure */
typedef struct Point {
    double x, y;
} Point;

/* Function involving a C data structure */
double distance(Point *p1, Point *p2) {
    return hypot(p1 -> x - p2 -> x, p1 -> y - p2 -> y);
}

###

# sample.py

import ctypes
import os

# Try to locate the .so file in the same directory as this file
_file = 'libsample.so'
path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = ctypes.cdll.LoadLibrary(_path)

# int gcd(int, int)
gcd = _mod.gcd 
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int

# int in_mandel(double, double, int)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int

# int divide(int, int, int *)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    return quot, rem.value

# void avg(double *, int n)
# Define a special type for the 'double *' argument
class DoubleArrayType:
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_', + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)
    
    # Cast from array.array objects
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))
    
    # Cast from lists/tuples
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val
    from_tuple = from_list

    # Cast from a numpy array
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

DoubleArray = DoubleArrayType()
_avg = _mod.avg
_avg.argtypes = (DoubleArray, ctypes.c_int)
_avg.restype = ctypes.c_double

def avg(values):
    return _avg(values, len(values))

# struct Point { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

# double distance(Point *, Point *)
distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double

###

import sample

sample.gcd(35, 42)
sample.in_mandel(0,0,500)
sample.in_mandel(2.0,1.0,500)
sample.divide(42, 8)
sample.avg([1, 2, 3])
p1 = sample.Point(1,2)
p2 = sample.Point(4,5)
sample.distance(p1,p2)

###

from ctypes.util import find_library
find_library('m')
find_library('pthread')
find_library('sample')

_mod = ctypes.cdll.LoadLibrary(_path)

# int in_mandel(double, double, int)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int

###

divide = _mod.divide
divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
x = 0
divide(10, 3, x)  # ctypes.ArgumentError

###

x = ctypes.c_int()
divide(10, 3, x)
x.value

###

# int divide(int, int, int *)
divide = _mod.divide
divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    return quot, rem.value

###

nums = [1, 2, 3]
a = (ctypes.c_double * len(nums))(*nums)
a[0]  # 1.0

###

import array
a = array.array('d', [1, 2, 3])
ptr_ = a.buffer_info()
ptr  # 4298687200
c.types.cast(ptr, ctypes.POINTER(ctypes.c_double))  # <__main__.LP_c_double object at 0x10069cd40>

###

import sample

sample.avg([1, 2, 3])

import array

sample.avg(array.array('d', [1, 2, 3]))
import numpy

sample.avg(numpy.array([1.0,2.0,3.0]))

###

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

###

p1 = sample.Point(1, 2)
p2 = sample.Point(4, 5)
p1.x  # 1.0
p1.y  # 2.0
sample.distance(p1, p2)
