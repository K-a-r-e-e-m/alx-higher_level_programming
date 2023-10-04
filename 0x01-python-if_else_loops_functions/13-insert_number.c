#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: The head node to access on all list.
 * @number: The number that you want to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *trv = *head;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	while (trv->next && newNode->n > trv->next->n)
		trv = trv->next;
	newNode->next = trv->next;
	trv->next = newNode;

	return (newNode);
}
