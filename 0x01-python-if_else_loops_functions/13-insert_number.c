#include "lists.h"
/**
 * insert_node - insert a node in order
 * @head: head of the linked list
 * @number: data needs to be stored
 * Return: new node
*/
listint_t *insert_node(listint_t **head, int number)
{listint_t *new, *prev = NULL, *current = *head;

current = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
if (*head == NULL)
{
*head = new;
return (new);
}
else
{
while (current->next != NULL)
{
if (current->n < number)
{
prev = current;
current = current->next;
}
else
{
if (prev != NULL)
{
prev->next = new;
new->next = current;
}
else
{
new->next = current;
*head = new;
}
break;
}}
if (new->next == NULL)
{current->next = new;
}}
return (new);
}
