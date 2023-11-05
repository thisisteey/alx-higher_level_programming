#include "lists.h"

/**
 * rev_listint - reverses a linked list
 * @head: pointer to the linked list
 * Return: pointer to the head of the reversed list
 */
void rev_listint(listint_t **head)
{
	listint_t *pnode = NULL;
	listint_t *currnode = *head;
	listint_t *nxtnode = NULL;

	while (currnode)
	{
		nxtnode = currnode->next;
		currnode->next = pnode;
		pnode = currnode;
		currnode = nxtnode;
	}
	*head = pnode;
}

/**
 * is_palindrome - checks a linked list if it is a palindrome
 * @head: pointer to the linked list
 * Return: 1 if its a palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head;
	listint_t *tmptr = *head, *revlist = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		hare = hare->next->next;
		if (hare == NULL)
		{
			revlist = tortoise->next;
			break;
		}
		if (hare->next == NULL)
		{
			revlist = tortoise->next->next;
			break;
		}
		tortoise = tortoise->next;
	}
	rev_listint(&revlist);
	while (revlist && tmptr)
	{
		if (tmptr->n == revlist->n)
		{
			revlist = revlist->next;
			tmptr = tmptr->next;
		}
		else
			return (0);
	}
	if (revlist == NULL)
		return (1);
	return (0);
}
