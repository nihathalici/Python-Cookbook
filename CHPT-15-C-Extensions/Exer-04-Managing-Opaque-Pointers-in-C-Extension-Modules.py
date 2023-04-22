# Exer-04-Managing-Opaque-Pointers-in-C-Extension-Modules

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point *p1, Point *p2);

###

/* Destructor function for points */
static void del_Point(PyObject *obj) {
    free(PyCapsule_GetPointer(obj, "Point"));
}

/* Utility functions */
static Point *PyPoint_AsPoint(PyObject *obj) {
    return (Point *) PyCapsule_GetPointer(obj, "Point");
}

static PyObject *PyPoint_FromPoint(Point *p, int must_free) {
    return PyCapsule_New(p, "Point", must_free ? del_Point : NULL);
}

/* Create a new Point object */
static PyObject *py_Point(PyObject *self, PyObject *args) {
    Point *p;
    double x, y;
    if (!PyArg_ParseTuple(args, "dd", &x, &y)) {
    return NULL;
    }
    p = (Point *) malloc(sizeof(Point));
    p->x = x;
    p->y = y;
    return PyPoint_FromPoint(p, 1);
}

static PyObject *py_distance(PyObject *self, PyObject *args) {
    Point *p1, *p2;
    PyObject *py_p1, *py_p2;
    double result;

    if (!PyArg_ParseTuple(args, "OO", &py_p1, &py_p2)) {
      return NULL;
    }
    if (!(p1 = PyPoint_AsPoint(py_p1))) {
      return NULL;
    } 
    if (!(p2 = PyPoint_AsPoint(py_p2))) {
      return NULL;
    }
    result = distance(p1, p2);
    return Py_BuildValue("d", result); 
}

###

import sample

p1 = sample.Point(2,3)
p2 = sample.Point(4,5)
p1  # <capsule object "Point" at ...
sample.distance(p1, p2)  # 2.8284271247461903