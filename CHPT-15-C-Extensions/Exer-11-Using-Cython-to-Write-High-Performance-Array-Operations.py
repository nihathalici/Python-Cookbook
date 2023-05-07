# Exer-11-Using-Cython-to-Write-High-Performance-Array-Operations

# sample.pyx (Cython)

cimport cython 

@cython.boundscheck(False)
@cython.wraparound(False)

cpdef clip(double[:] a, double min, double max, double[:] out):
    """
    Clip the values in a to be between min and max. Result in out
    """
    if min > max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        if a[i] < min:
            out[i] = min
        elif a[i] > max:
            out[i] = max
        else:
            out[i] = a[i]

###

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension('sample', 
              ['sample.pyx'])
]

setup(
    name = 'Sample app',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

###

# array module example

import sample
import array

a = array.array('d', [1,-3,4,7,2,0])
a  # array('d', [1.0, -3.0, 4.0, 7.0, 2.0, 0.0])

sample.clip(a, 1, 4, a)
a  # array('d', [1.0, 1.0, 4.0, 4.0, 2.0, 1.0])

# numpy example
import numpy

b = numpy.random.uniform(-10, 10, size=1000000)
b  # array([-9.55546017, 7.45599334, 0.69248932, ..., 0.69583148, -3.86290931, 2.37266888])
c = numpy.zeros_like(b)
c  # array([ 0., 0., 0., ..., 0., 0., 0.])

sample.clip(b, -5, 5, c)
c  # array([-5. , 5. , 0.69248932, ..., 0.69583148, -3.86290931, 2.37266888])

min(c)  # -5.0
max(c)  # 5.0

timeit('numpy.clip(b,-5,5,c)', 'from __main__ import b, c, numpy', number = 1000)

timeit('sample.clip(b,-5,5,c)', 'from __main__ import b, c, sample', number = 1000)

###

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):

    if min > max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        out[i] = (a[i] if a[i] < max else max) if a[i] > min else min 

###

void clip(double *a, int n, double min, double max, double *out) {
    double x;
    for (; n >= 0; n--, a++, out++) {
        x = *a;
        *out = x > max ? max : ( x < min ? min : x );
    }
}

###

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):
    if min > max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    with nogil:
        for i in range(a.shape[0]):
            out[i] = (a[i] if a[i] < max else max) if a[i] > min else min 

###

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip2d(double[:,:] a, double min, double max, double[:,:] out):
    if min > max:
        raise ValueError("min must be <= max")
    for n in range(a.ndim):
        if a.shape[n] != out.shape[n]:
            raise TypeError("a and out have different shapes")
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i,j] < min:
                out[i,j] = min
            elif a[i,j] > max:
                out[i,j] = max
            else:
                out[i,j] = a[i,j]

    

    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        out[i] = (a[i] if a[i] < max else max) if a[i] > min else min 

