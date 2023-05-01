# Exer-08-Mixing-Threads-from-C-and-Python

#include <Python.h>

...
if (!PyEval_ThreadsInitialized()) {
    PyEval_InitThreads();
}
...

###

...
/* Make sure we own the GIL */
PyGILState_STATE state = PyGILState_Ensure();

/* Use functions in the interpreter */
...
/* Restore previous GIL state and return */
PyGILState_Release(state);