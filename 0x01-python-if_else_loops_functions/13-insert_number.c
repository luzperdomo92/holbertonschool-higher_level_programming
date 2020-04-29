#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert node in sorted list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: the node created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *iterator;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return(NULL);
	
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return(new_node);
	}
		

	iterator = *head;
	
	if(iterator->n > number)
	{
		new_node->next = iterator;
		*head = new_node;
		return (new_node);
	}

	while (iterator != NULL)
	{
		if (iterator->n < number &&
				(iterator->next== NULL || iterator->next->n > number))
		{
			new_node->next = iterator->next;
			iterator->next = new_node;
			break;
		}
		iterator = iterator->next;
	}
	return (new_node);
}
