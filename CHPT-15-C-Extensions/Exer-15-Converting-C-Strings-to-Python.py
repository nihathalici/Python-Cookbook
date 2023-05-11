# Exer-15-Converting-C-Strings-to-Python

char *s;  /* Pointer to C string data */
int len;  /* Length of data */

/* Make a bytes object */
PyObject *obj = Py_BuildValue("y#", s, len);

PyObject *obj = Py_BuildValue("s#", s, len);

PyObject *obj = PyUnicode_Decode(s, len, "encoding", "errors");

/* Examples /*
obj = PyUnicode_Decode(s, len, "latin-1", "strict");
obj = PyUnicode_Decode(s, len, "ascii", "ignore");

###

wchar_t *w;  /* Wide character string */
int len;  /* Length */

PyObject *obj = Py_BuildValue("u#", w, len);

PyObject *obj = PyUnicode_FromWideChar(w, len);