#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some bacis info about a python list
 * @p: pointer to the pythin list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *itm;
	PyListObject *listobj = (PyListObject *)p;
	int idx, listsz, listalloc;

	listsz = Py_SIZE(p);
	listalloc = listobj->allocated;
	printf("[*] Size of the Python List = %d\n", listsz);
	printf("[*} Allocated = %d\n", listalloc);
	for (idx = 0 ; idx < listsz ; idx++)
	{
		itm = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", idx, Py_TYPE(itm)->tp_name);
	}
}
