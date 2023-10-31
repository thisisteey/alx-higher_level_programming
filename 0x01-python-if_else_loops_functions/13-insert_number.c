#include "lists.h"

/**
 * insert_node - function that adds a number to a sorted linked list
 * @head: pointer to the linked list
 * @number: number to be added to the sorted linked list
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cnode = *head, *nnode;

	nnode = malloc(sizeof(listint_t));
	if (nnode == NULL)
		return (NULL);
	nnode->n = number;
	if (cnode == NULL || cnode->n >= number)
	{
		nnode->next = cnode;
		*head = nnode;
		return (nnode);
	}
	while (cnode && cnode->next && cnode->next->n < number)
		cnode = cnode->next;
	nnode->next = cnode->next;
	cnode->next = nnode;

	return (nnode);
}
