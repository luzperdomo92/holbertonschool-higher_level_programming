#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: linked list head
 *
 * Return: 1 if it has a cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *ahead = list;
	listint_t *behind = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	ahead = list->next->next;
	behind = behind->next;
	while (ahead != NULL && ahead->next != NULL)
	{
		if (ahead == behind)
		{
			return (1);
		}
		ahead = ahead->next->next;
		behind = behind->next;
	}

	return (0);
}
