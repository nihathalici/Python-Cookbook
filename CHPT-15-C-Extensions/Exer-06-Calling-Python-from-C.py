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

