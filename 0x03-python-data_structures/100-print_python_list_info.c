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
    long int size_of_list = PyList_Size(p);
    long int allocated = ((PyListObject *)p)->allocated;
    int i;

    printf("[*] Size of the Python List = %ld\n", size_of_list);
    printf("[*] Allocated = %ld\n", allocated);
    for (i = 0; i < size_of_list; i++)
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
