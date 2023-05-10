# Exer-13-Passing-NULL-Terminated-Strings-to-C-Libraries

void print_chars(char *s) {
    while (*s) {
        printf("%2x ", (unsigned char) *s);
        s++;
    }
    printf("\n");
}

print_chars("Hello");  # 48 65 6c 6c 6f

###

static PyObject *py_print_chars(PyObject *self, PyObject *args) {
    char *s;

    if (!PyArg_ParseTuple(args, "y", &s)) {
        return NULL;
    }
    print_chars(s);
    Py_RETURN_NONE;
}

###

print_chars('Hello World')  # 48 65 6c 6c 6f 20 57 6f 72 6c 64
print_chars('Spicy Jalape\u00f1o')  # 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f
print_chars('Hello\x00World')  # TypeError: must be str without null characters, not str
print_chars(b'Hello World')  # TypeError: must be str, not bytes

###

PyObject *obj;

{
    char *s;
    s = PyBytes_AsString(o);
    if (!s) {
        return NULL;  /* TypeError already raised */
    }
    print_chars(s);
}

/* Conversion to UTF-8 bytes from a string */
{
    PyObject *bytes;
    char *s;
    if (!PyUnicode_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected string");
        return NULL;
    }
    bytes = PyUnicode_AsUTF8String(obj);
    s = PyBytes_AsString(bytes);
    print_chars(s);
    Py_DECREF(bytes);
}

###

import sys 

s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s) # 87

print_chars(s) # # Passing string
sys.getsizeof(s) # increased size: 103

static PyObject *py_print_chars(PyObject *self, PyObject *args) {
    PyObject *o, *bytes;
    char *s;

    if (!PyArg_ParseTuple(args, "U", &o)) {
        return NULL;
    }
    bytes = PyUnicode_AsUTF8String(o);
    s = PyBytes_AsString(bytes);
    print_chars(s);
    Py_DECREF(bytes);
    Py_RETURN_NONE;
}

####

import sys 

s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s) # 87

print_chars(s) # 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f
sys.getsizeof(s) # 87

###

import ctypes

lib = ctypes.cdll.LoadLibrary("./libsample.so")
print_chars = lib.print_chars
print_chars.argtypes = (ctypes.c_char_p,)
print_chars(b"Hello World")   # 48 65 6c 6c 6f 20 57 6f 72 6c 64
print_chars(b"Hello\x00World")  # 48 65 6c 6c 6f
print_chars('Hello World')  # ctypes.ArgumentError: argument 1: <class 'TypeError'>: wrong type

print_chars('Hello World'.encode('utf-8'))  # 48 65 6c 6c 6f 20 57 6f 72 6c 64


