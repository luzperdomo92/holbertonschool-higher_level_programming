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
	listint_t *start;
	listint_t *ahead;
	if(list == NULL || list->next == NULL)
	{
		return (0);
	}

	ahead = list->next;
	while (ahead->next != NULL)
	{
		start = list;
		while (start->next != ahead)
		{
			if (ahead->next == start)
			{
				return (1);
			}
			start = start->next;
		}

		ahead = ahead->next;
	}
	return (0);
}
