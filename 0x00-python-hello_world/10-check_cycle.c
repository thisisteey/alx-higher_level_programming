#include "lists.h"

/**
 * check_cycle - function checks if a list has a cycle in it
 * @list: pointer to the linked list node
 * Return: 0 if there is no cycle and 1 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
	{
		return (0);
	}
	hare = list->next;
	tortoise = list;

	while (hare != NULL && hare->next != NULL && tortoise != NULL)
	{
		if (hare == tortoise)
		{
			return (1);
		}
		hare = hare->next->next;
		tortoise = tortoise->next;
	}
	return (0);
}
