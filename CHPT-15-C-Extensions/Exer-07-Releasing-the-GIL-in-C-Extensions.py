# Exer-07-Releasing-the-GIL-in-C-Extensions

#include "Python.h"
...

PyObject *pyfunc(PyObject *self, PyObject *args) {
    ...
    Py_BEGIN_ALLOW_THREADS
    // Threaded C code.  Must not use Python API functions
    ...
    Py_END_ALLOW_THREADS
    ...
    return result;
}