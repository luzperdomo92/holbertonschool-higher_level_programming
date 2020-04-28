#include "lists.h"

int check_cycle(listint_t *list)
{
	int head_n;
	if(list == NULL)
	{
		return (0);
	}

	head_n = list->n;
	while(list->next != NULL)
	{
		if (list->next->n == head_n)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
