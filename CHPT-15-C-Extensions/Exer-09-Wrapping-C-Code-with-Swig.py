# Exer-09-Wrapping-C-Code-with-Swig

/* sample.h */

#include <math.h>
extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point *p1, Point *p2);

###

// sample.i - Swig interface
%module sample
%{
#include "sample.h"    
%}

/* Customizations */
%extend Point {
    /* Constructor for Point objects */
    Point(double x, double y) {
        Point *p = (Point *) malloc(sizeof(Point));
        p -> x = x;
        p -> y = y;
        return p;
    };
};

/* Map int *remainder as an output argument */
%include typemaps.i 
%apply int *OUTPUT { int * remainder };
/* Map the argument pattern (double *a, int n) to arrays */
%typemap(in) (double *a, int n)(Py_buffer view) {
    view.obj = NULL;
    if (PyObject_GetBuffer($input, &view, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {
        SWIG_fail;
    }
    if (strcmp(view.format, "d") != 0) {
        PyErr_SetString(PyExc_TypeError, "Expected an array of doubles");
        SWIG_fail;
    }
    $1 = (double *) view.buf;
    $2 = view.len / sizeof(double);
}

%typemag(freearg) (double *a, int n) {
    if (view$argnum.obj) {
        PyBuffer_Release(&view$argnum);
    }
}

/* C declarations to be included in the extension module */

extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point *p1, Point *p2)

###

# bash % swig -python -py3 sample.i # output: sample_wrap.c and sample.py

###

# setup.py
from distutils.core import setup, Extension

setup(name='sample',
      py_modules=['sample.py'],
      ext_modules=[
          Extension('_sample,'
                    ['sample_wrap.c'],
                    include_dirs = [],
                    define_macros = [],
                    undef_macros = [],
                    library_dirs = [],
                    libraries = ['sample']
                    )
            ]
    )

bash % python3 setup.py build_ext --inplace

###

import sample

sample.gcd(42,8)  # 2
sample.divide(42, 8)  # [5, 2]
p1 = sample.Point(2, 3)
p2 = sample.Point(4, 5)
sample.distance(p1, p2)
p1.x  # 2.0
p1.y  # 3.0

import array

a = array.array('d', [1, 2, 3])
sample.avg(a) # 2.0

###

%module sample
%{
#include "sample.h"    
%}

###

%module sample
%{
#include "sample.h"    
%}
...
extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point *p1, Point *p2)

###

p1 = sample.Point(2, 3)

###

# Usage if %extend Point is omitted
p1 = sample.Point()
p1.x = 2.0
p1.y = 3
