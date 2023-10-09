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
	int n = 0, j = 0, k = 0, arr[1000]; /* Let 1000 is max value arr can hold */

	while (trv) /* Count the length of list (n) */
		trv = trv->next, n++;
	trv = *head; /* Make (trv) point to first node */

	j = (n / 2) - 1; /* j is last index of array */
	while (trv && j + 1)
	{
		arr[j--] = trv->n; /* Fill the array from last to first */
		trv = trv->next;
	}

	(n % 2 ? (trv = trv->next) : trv); /* If n is odd move to next node */
	while (trv)
	{
		if (trv->n == arr[k]) /* k start from 0 */
			trv = trv->next, k++;
		else /* If The (node value) and (array value) not equal at any index */
			return (0);
	}
	return (1); /* If previous while loop end without goes to else condition */
}
