# Exer-19-Reading-File-Like-Objects-from-C

#define CHUNK_SIZE 8192
/* Consume a "file-like" object and write bytes to stdout */
static PyObject *py_consume_file(PyObject *self, PyObject *args) {
    PyObject *obj;
    PyObject *read_meth;
    PyObject *result = NULL;
    PyObject *read_args;

    if (!PyArg_ParseTuple(args, "O", &obj)) {
        return NULL;
    }

    /* Get the read method of the passed object */
    if ((read_meth = PyObject_GetAttrString(obj, "read")) == NULL) {
        return NULL;
    }

    /* Build the argument list to read() */
    read_args = Py_BuildValue("(i)", CHUNK_SIZE);
    while (1) {
        PyObject *data;
        PyObject *enc_data;
        char *buf;
        Py_ssize_t len;

        /* Call read() */
        if ((data = PyObject_Call(read_meth, read_args, NULL)) == NULL) {
            goto final;
        }

        /* Check for EOF */
        if (PySequence_Length(data) == 0) {
            Py_DECREF(data);
            break;
        }

        /* Encode Unicode as Bytes for C */
        if ((enc_data = PyUnicode_AsEncodedString(data, "utf-8", "strict")) == NULL) {
            Py_DECREF(data);
            goto final;
        }

        /* Extract underlying buffer data */
        PyBytes_AsStringAndSize(enc_data, &buf, &len);

        /* Write to stdout (replace with something more useful) */
        write(1, buf, len);

        /* Cleanup */
        Py_DECREF(enc_data);
        Py_DECREF(data);
    }
    result = Py_BuildValue("");

    final:
      /* Cleanup */
      Py_DECREF(read_meth);
      Py_DECREF(read_args);
      return result;
}

###

import io 
f = io.StringIO('Hello\nWorld\n')
import sample
sample.consume_file(f)

###

...
/* Call read() */
if ((data = PyObject_Call(read_meth, read_args, NULL)) == NULL) {
   goto final;
}

/* Check for EOF */
if (PySequence_Length(data) == 0) {
   Py_DECREF(data);
   break;
}
if (!PyBytes_Check(data)) {
   Py_DECREF(data);
   PyErr_SetString(PyExc_IOError, "File must be in binary mode");
   goto final;
}

/* Extract underlying buffer data */
PyBytes_AsStringAndSize(data, &buf, &len);
...