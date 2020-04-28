#include "lists.h"

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
