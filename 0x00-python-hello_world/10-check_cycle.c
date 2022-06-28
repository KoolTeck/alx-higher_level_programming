#include "lists.h"

/**
 * check_cycle - checks if a singly list contains a circle
 *
 * @list: the list to check
 *
 * Return: Always 0 if not found, 1 if found
 */
int check_cycle(listint_t *list)
{
listint_t *snail, *snake;

snail = list;
snake = list;
while (snake && snail && snail->next)
{
if (snail == NULL)
return (0);
snail = snail->next;
snake = snake->next->next;
if (snake == snail)
return (1);
}
return (0);
}
