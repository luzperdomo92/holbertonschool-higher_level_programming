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
	int i;
	int size = 0;
	int elements[1024];

	if (iterable_node == NULL)
		return (1);

	while (iterable_node != NULL)
	{
		elements[size] = iterable_node->n;
		iterable_node = iterable_node->next;
		size++;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (elements[i] != elements[size - 1 - i])
		{
			return (0);
		}

	}
	return (1);
}
