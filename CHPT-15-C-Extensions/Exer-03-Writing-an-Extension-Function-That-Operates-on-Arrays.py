# Exer-03-Writing-an-Extension-Function-That-Operates-on-Arrays

/* Call double avg(double *, int) */
static PyObject *py_avg(PyObject *self, PyObject *args) {
    PyObject *bufobj;
    Py_buffer view;
    double result;
    /* Get the passed Python object */
    if (!PyArg_ParseTuple(args, "0", &bufobj)) {
    return NULL;
    }
}

/* Attempt to extract buffer information from it */
if (PyObject_GetBuffer(bufobj, &view,
    PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {
    return NULL; 
}

if (view.ndim != 1) {
        PyErr_SetString(PyExc_TypeError, "Expected a 1-dimensional array");
        PyBuffer_Release(&view);
        return NULL;
}

/* Check the type of items in the array */
if (strcmp(view.format, "d") != 0) {
        PyErr_SetString(PyExc_TypeError, "Expected an array of doubles");
        PyBuffer_Release(&view);
        return NULL;
}

/* Pass the raw buffer and size to the C function */
result = avg(view.buf, view.shape[0]);

/* Indicate we're done working with the buffer */
PyBuffer_Release(&view);
return Py_BuildValue("d", result);

###

import array 

avg(array.array('d', [1, 2, 3]))  # 2.0

import numpy

avg(numpy.array([1.0, 2.0, 3.0]))  # 2.0

avg([1, 2, 3])  # TypeError

avg(b'Hello')  # TypeError

avg(a[:,2])  # ValueError

sample.avg(a)  # TypeError

sample.avg(a[0])  # 2.0

###

typedef struct bufferinfo {
    void *buf;                  /* Pointer to buffer memory */
    PyObject *obj;              /* Python object that is the owner */
    Py_ssize_t len;             /* Total size in bytes */
    Py_ssize_t itemsize;        /* Size in bytes of a single item */
    int readonly;               /* Read-only access flag */
    int ndim;                   /* Number of dimensions */
    char *format;               /* struct code of a single item */
    Py_ssize_t *shape;          /* Array containing dimensions */
    Py_ssize_t *strides;        /* Array containing strides */
    Py_ssize_t *suboffsets;     /* Array containing suboffsets */

} Py_buffer;
