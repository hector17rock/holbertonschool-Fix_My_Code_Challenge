#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t list
 * @head: pointer to pointer to head of list
 * @index: zero-based index of node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	node = *head;

	/* Walk to the node at `index` */
	for (i = 0; node != NULL && i < index; i++)
		node = node->next;

	/* If index is out of range */
	if (node == NULL)
		return (-1);

	/* Stitch neighbors together correctly */
	if (node->prev != NULL)
		node->prev->next = node->next;
	else
		*head = node->next;           /* deleting the head */

	if (node->next != NULL)
		node->next->prev = node->prev;

	free(node);

	/* Ensure new head (if any) has prev == NULL */
	if (*head != NULL)
		(*head)->prev = NULL;

	return (1);
}
