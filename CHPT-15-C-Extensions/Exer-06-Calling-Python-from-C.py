# Exer-06-Calling-Python-from-C

#include <Python.h>

/* Execute func(x,y) in the Python interpreter.  The
   arguments and return result of the function must
   be Python floats */

double call_func(PyObject *func, double x, double y) {
   PyObject *args;
   PyObject *kwargs;
   PyObject *result = 0;
   double retval;

   /* Make sure we own the GIL */
   PyGILState_STATE state = PyGILState_Ensure();
   /* Verify that func is a proper callable */
   if (!PyCallable_Check(func)) {
     fprintf(stderr, "call_func: expected a callable\n");
     goto fail;
   }
   /* Build arguments */
   args = Py_BuildValue("(dd)", x, y);
   kwargs = NULL;

   /* Call the function */
   result = PyObject_Call(func, args, kwargs);
   Py_DECREF(args);
   Py_XDECREF(kwargs);

   /* Check for Python exceptions (if any) */
   if (PyErr_Occurred()) {
     PyErr_Print();
     goto fail;
   }

   /* Verify the result is a float object */
   if (!PyFloat_Check(result)) {
   fprintf(stderr, "call_func: callable didn't return a float\n");
   goto fail;
   }

   /* Create the return value */
   retval = PyFloat_AsDouble(result);
   Py_DECREF(result);

   /* Restore previous GIL state and return */
   PyGILState_Release(state);
   return retval;

fail:
   Py_XDECREF(result);
   PYGILState_Release(state);
   abort();
   
}

###

#include <Python.h>

/* Definition of call_func() same as above */
...

/* Load a symbol from a module */
PyObject *import_name(const char *modname, const char *symbol) {
   PyObject *u_name, *module;
   u_name = PyUnicode_FromString(modname);
   module = PyImport_Import(u_name);
   Py_DECREF(u_name);
   return PyObject_GetAttrString(module, symbol);
}

/* Simple embedding example */
int main() {
   PyObject *pow_func;
   double x;

   Py_Initialize();
   /* Get a reference to the math.pow function */
   pow_func = import_name("math", "pow");
   
   /* Call it using our call_func() code */
   for (x = 0.0; x < 10.0; x += 0.1) {
      printf("%0.2f %0.2f\n", x, call_func(pow_func, x, 2.0));
   }
   /* Done */
   PyDECREF(pow_func);
   Py_Finalize();
   return 0;
}

###
# Makefile

all::
  cc -g embed.c -I/usr/local/include/python3.3m \
  -L/usr/local/lib/python3.3/config-3.3m -lpython3.3m

###

/* Extension function for testing the C-Python callback */
PyObject *py_call_func(PyObject *self, PyObject *args) {
   PyObject *func;

   double x, y, result;
   if (!PyArg_ParseTuple(args, "Odd", &func, &x, &y)) {
      return NULL;
   }
   result = call_func(func, x, y);
   return PyBuildValue("d", result); 
}

###

import sample

def add(x, y):
  return x + y 

sample.call_func(add, 3, 4)

###

double call_func(PyObject *func, double x, double y) {
   ...
   /* Verify that func is a proper callable */
   if (!PyCallable_Check(func)) {
      fprintf(stderror, "call_func: expected a callable\n");
      goto fail;
   }
   ...

}

###

double call_func(PyObject *func, double x, double y) {
   PyObject *args;
   PyObject *kwargs;
   
   ...
   /* Build arguments */
   args = Py_BuildValue('(dd)', x, y);
   kwargs = NULL;

   /* Call the function */
   result = PyObject_Call(func, args, kwargs);
   Py_DECREF(args);
   Py_XDECREF(kwargs);
   ...
}

###

  /* Check for Python exceptions (if any) */
  if (PyErr_Occurred()) {
     PyErr_Print();
     goto fail;
  }
  ...
fail:
  PyGILState_Release(state);
  abort();

###

double call_func(PyObject *func, double x, double y) {
   ...
   double retval;

   /* Make sure we own the GIL */
   PyGILState_STATE state = PyGILState_Ensure();
   ...
   /* Code that uses Python C API functions */
   ...
   /* Restore previous GIL state and return */
   PyGILState_Release(state);
   return retval;

fail:
    PyGILState_Release(state);
    abort();
}
