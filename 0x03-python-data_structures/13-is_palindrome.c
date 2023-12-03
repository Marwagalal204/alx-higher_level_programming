#include"lists.h"
/**
 * is_palindrome - A c function checks if a linked list is palindrome.
 * @head: head of the list
 * Return: 1 for is palindrome, 0 for not a palindrone.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL, *temp = NULL;

if (*head == NULL || (*head)->next == NULL)
{
return (1);
}

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}
if (fast != NULL)
{
slow = slow->next;
}
while (prev != NULL && slow != NULL)
{
if (prev->n != slow->n)
{
return (0);
}
prev = prev->next;
slow = slow->next;
}
return (1);
}
