#include "lists.h"

/**
 * is_palindrome - check palindrome
 *
 * @head: The head of linked list
 *
 * Description: This function check if the given linked list
 * is palindrome or not.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *trv = *head;
	int n = 0, m = 0, start, j = 0, k = 0, arr[1000];

	if (!*head || !(*head)->next)
		return (1);
	while (trv)
	{
		trv = trv->next;
		n++;
	}
	start = (n / 2); /* 2 */
	j = start - 1; /* 3 */
	trv = *head;
	while (trv)
	{
		if (m == start) /* m = 0, start = 4 */
			break;
		arr[j] = trv->n;
		m++, j--; 
		trv = trv->next;

	}
	(n % 2 ? (trv = trv->next) : trv);
	while (trv)
	{
		if (trv->n == arr[k])
		{
			trv = trv->next;
			k++;
		}
		else
			return (0);
	}
	return (1);
}
