# Exer-02-Writing-a-Simple-C-Extension-Module

/* sample.h * /

#include <math.h>

extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n)
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point *p1, Point *p2);

###

#include "Python.h"
#include "sample.h"

/* int gcd(int, int) */
static PyObject *py_gcd(PyObject *self, PyObject *args) {
    int x, y, result;

    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
    return NULL;
    }
    result = gcd(x, y);
    return Py_BuildValue("i", result);
}

/* int in_mandel(double, double, int) */
static PyObject *py_in_mandel(PyObject *self, PyObject *args) {
    double x0, y0;
    int n;
    int result;

    if (!PyArg_ParseTuple(args, "ddi", &x0, &y0, &n)) {
    return NULL;
    }
    result = in_mandel(x0, y0, n)
    return Py_BuildValue("i", result);
}

/* int divide(int, int, int *) */
static PyObject *py_divide(PyObject *self, PyObject *args) {
    int a, b, quotient, remainder;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
    return NULL;
    }
    quotient = divide(a, b, &remainder);
    return Py_BuildValue("(ii)", quotient, remainder); 
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"gcd", py_gcd, METH_VARARGS, "Greatest common divisor"},
    {"in_mandel", py_in_mandel, METH_VARARGS, "Mandelbrot test"},
    {"divide", py_divide, METH_VARARGS, "Integer division"},
    {NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
    PyModuleDef_HEAD_INIT,
    "sample",               /* name of module */
    "A sample module,"      /* Doc string (may be NULL) */
    -1,                     /* Size of per-interpreter state or -1 */
    SampleMethods           /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void) {
    return PyModule_Create(&samplemodule);
}

###

# setup.py

from distutils.core import setup, Extension

setup(name="sample",
      ext_modules=[
    Extension("sample",
              ["pysample.c"],
              include_dirs = ["/some/dir"],
              define_macros = [("FOO", "1")],
              undef_macros = ["BAR"],
              library_dirs = ["/usr/local/lib"],
              libraries = ["sample"]
              )
      ]
)

###

# build the resulting library
# bash % python3 setup.py build_ext --inplace

###

import sample
sample.gcd(35, 42)
sample.in_mandel(0, 0, 500)
sample.in_mandel(2.0, 1.0, 500)