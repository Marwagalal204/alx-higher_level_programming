#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *fast, *slow;
    fast = slow = list;

    if (list == NULL)
        return (0);
        while (slow != NULL && fast != NULL && fast->next != NULL)
        {
        slow = slow->next;
        fast = fast->next->next;
        
        if (fast == slow)
            return (1);
        }
        return (0);
}
