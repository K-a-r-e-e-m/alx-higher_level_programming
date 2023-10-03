#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: List of node structure.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *second = list, *first = list;

	if (list == NULL)
		return (0);
	while (second != NULL && first != NULL && first->next != NULL)
	{
		second = second->next;
		first = first->next->next;
		if (second == first)
			return (1);
	}
	return (0);
}
