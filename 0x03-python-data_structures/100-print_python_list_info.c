#define PY_SSIZE_T_CLEAN
#include "Python.h"

/**
 * print_python_list_info - prints some bacis info about a python list
 * @p: pointer to the python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int listsz, i, listalloc;
	PyObject *listobj;

	listsz = Py_SIZE(p);
	listalloc = ((PyListObject *) p)->allocated;
	printf("[*] Size of the Python List = %d\n", listsz);
	printf("[*} Allocated = %d\n", listalloc);
	for (i = 0 ; i < listsz ; i++)
	{
		printf("Element %d: ", i);
		listobj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(listobj)->tp_name);
	}
}
