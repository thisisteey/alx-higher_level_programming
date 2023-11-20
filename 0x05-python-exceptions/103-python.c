#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - prints information about a PyFloatObject
 * @p: pointer to the PyObject representing a PyFloatObject
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double fltval = 0;
	char *fltstr = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	fltval = ((PyFloatObject *)p)->ob_fval;
	fltstr = PyOS_double_to_string(fltval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", fltstr);
}

/**
 * print_python_bytes - prints information about a PyBytesObject
 * @p: pointer to the PyObject representing a PyBytesObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytsz = 0, idx = 0;
	char *bytstr = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytsz = PyBytes_Size(p);
	printf("  size: %zd\n", bytsz);
	bytstr = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", bytstr);
	printf("  first %zd bytes:", bytsz < 10 ? bytsz + 1 : 10);
	while (idx < bytsz + 1 && idx < 10)
	{
		printf(" %02hhx", bytstr[idx]);
		idx++;
	}
	printf("\n");
}

/**
 * print_python_list - prints information about a PyListObject
 * @p: pointer to the PyObject representing a PyListObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t lstsz = 0;
	PyObject *lstitm;
	int idx = 0;

	fflush(stdout);
	printf("[*] Python List info\n");
	if (PyList_CheckExact(p))
	{
		lstsz = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", lstsz);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (idx < lstsz)
		{
			lstitm = PyList_GET_ITEM(p, idx);
			printf("Element %d: %s\n", idx, lstitm->ob_type->tp_name);
			if (PyBytes_Check(lstitm))
				print_python_bytes(lstitm);
			else if (PyFloat_Check(lstitm))
				print_python_float(lstitm);
			idx++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
