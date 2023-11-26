#include "Python.h"

/**
 * print_python_string - prints information about a PyStringObject
 * @p: pointer to the PyObject representing the PyStringObject
 * Return: void
 */
void print_python_string(PyObject *p)
{
	long int strlent;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	strlent = ((PyASCIIObject *)(p))->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", strlent);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &strlent));
}
