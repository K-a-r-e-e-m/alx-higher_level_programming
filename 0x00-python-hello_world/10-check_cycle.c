#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: List of node structure.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list, *trav = list;

	while (trav != NULL)
	{
		trav = trav->next;
		if (trav == first)
			return (1);
	}
	return (0);
}
