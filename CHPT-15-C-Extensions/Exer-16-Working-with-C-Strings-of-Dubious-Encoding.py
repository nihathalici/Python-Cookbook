# Exer-16-Working-with-C-Strings-of-Dubious-Encoding

/* Some dubious string data (malformed UTF-8) */
const char *sdata = "Spicy Jalape\xc3\xb1o\xae";
int slen = 16;

/* Output character data */
void print_chars(char *s, int len) {
    int n = 0;
    while (n < len) {
        printf("%2x ", (unsigned char) s[n]);
        n++
    }
    printf("\n");
}

###

/* Return the C string back to Python */
static PyObject *py_retstr(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, "")) {
        return NULL;
    }
    return PyUnicode_Decode(sdata, slen, "utf-8", "surrogateescape");
}

/* Wrapper for the print_chars() function */
static PyObject *py_print_chars(PyObject *self, PyObject *args) {
    PyObject *obj, *bytes;
    char *s = 0;
    Py_ssize_t len;

    if (!PyArg_ParseTuple(args, "U", &obj)) {
        return NULL;
    }

    if ((bytes = PyUnicode_AsEncodedString(obj, "utf-8", "surrogateescape"))
          == NULL) {
              return NULL;
    }
    PyBytes_AsStringAndSize(bytes, &s, &len);
    print_chars(s, len);
    Py_DECREF(bytes);
    Py_RETURN_NONE;
}

###

s = retstr()
s # 'Spicy Jalapeño\udcae'
print_chars(s)  # 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f ae

###

raw = b'Spicy Jalape\xc3\xb1o\xae'
raw.decode("utf-8", "ignore")  # 'Spicy Jalapeño'
raw.decode("utf-8", "replace") # 'Spicy Jalapeño?'
raw.decode("utf-8", "surrogateescape")  # 'Spicy Jalapeño\udcae'

###

s = raw.decode("utf-8", "surrogateescape")
print(s)  # UnicodeEncodeError: 'utf-8' codec can't encode character '\udcae'

###
s  # 'Spicy Jalapeño\udcae'
s.encode('utf-8', "surrogateescape")  # b'Spicy Jalape\xc3\xb1o\xae'
