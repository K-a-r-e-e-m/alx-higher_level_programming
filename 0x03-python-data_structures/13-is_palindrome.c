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
	int n = 0, m = 0, start = 0;
	listint_t *trv = *head;

	while (trv)
	{
		trv = trv->next;
		n++;
	}
	if (n % 2)
		start = (n / 2) + 2;
	else
		start = (n / 2) + 1;
	trv = *head;
	int arr[n / 2];
	int j = n / 2 - 1;

	while (trv)
	{
		if (m == start - 1)
			break;
		arr[j] = trv->n;
		m++;
		j--;
		trv = trv->next;
	}

	j = 0;
	while (trv)
	{
		if (trv->n == arr[j])
		{
			trv = trv->next;
			j++;
		}
		else
			return (0);
	}
	return (1);
}
