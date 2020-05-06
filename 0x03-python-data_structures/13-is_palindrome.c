#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *add_node(listint_t **head, int n);

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *iterable_node = *head;
	listint_t *inverse_node;
	listint_t *inverse_node_disposable;
	int size, i;

	if (iterable_node == NULL)
		return (1);

	while (iterable_node != NULL)
	{
		add_node(&inverse_node, iterable_node->n);
		iterable_node = iterable_node->next;
		size++;
	}

	inverse_node_disposable = inverse_node;
	iterable_node = *head;
	for (i = 0; i <= size / 2; i++)
	{
		if (iterable_node->n != inverse_node->n)
		{
			free_listint(inverse_node_disposable);
			return (0);
		}
		iterable_node = iterable_node->next;
		inverse_node = inverse_node->next;
	}
	return (1);
}

/**
 * add_node - adds a new node at the beginning of a listint_t list
 * @head: start of the linked list
 * @n: int to be set as attribute of the next head.
 * Return: the number of nodes.
 */
listint_t *add_node(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}
