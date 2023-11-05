#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some bacis info about a python list
 * @p: pointer to the pythin list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int list_sz = PyList_Size(p);
	int idx;
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Size of the python List = %li\n", list_sz);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	for (idx = 0 ; idx < list_sz ; idx++)
		printf("Element %i: %s\n", idx, Py_TYPE(list_obj->ob_item[idx])->tp_name);
}
