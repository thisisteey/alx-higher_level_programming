#include "lists.h"

/**
 * check_cycle - function checks if a list has a cycle in it
 * @list: pointer to the linked list node
 * Return: 0 if there is no cycle and 1 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!list)
		return (0);
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
