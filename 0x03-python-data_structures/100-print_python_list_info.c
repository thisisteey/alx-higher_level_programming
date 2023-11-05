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
	PyObject *item;
	PyListObject *listobj = (PyListObject *)p;
	int i, listsz, listalloc;

	listsz = Py_SIZE(p);
	listalloc = listobj->allocated;
	printf("[*] Size of the Python List = %d\n", listsz);
	printf("[*} Allocated = %d\n", listalloc);
	for (i = 0 ; i < listsz ; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
