#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - This function prints some basic
 * info about Python lists.
 * @p: Python list object 
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size_of_list = PyList_GET_SIZE(p);
    PyListObject *allocated = ((PyListObject *)p)->allocated;
    size_t i;

    printf("[*] Size of the Python List = %ld", size_of_list);
    printf("[*] Allocated = %ld", allocated);
    for (i = 0; i < size_of_list; i++)
        printf("Element %lu: %s", i, PyList_GetItem(p, i));
}
