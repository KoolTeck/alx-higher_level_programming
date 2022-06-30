#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number in listint_t
 * @head: the node list head
 * @number: the number to insert
 *
 * Return: the address of the new node or NULL on error
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current;
listint_t *new, *prev;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
current = *head;
 if (*head == NULL)
   {
     *head = new;
   }
 else if (number < 0)
   {
     *head = new;
     new->next = current;
   }
 else
   {
   while (current->next != NULL)
   {
     if (current->n > number)
       {
	 new->next = current;
	 prev->next = new;
	 return (new);
       }
     prev = current;
     current = current->next;
   }
   current->next = new;
}

return (new);
}
