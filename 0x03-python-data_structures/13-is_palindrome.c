#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head node
 * Return: 1 on true l, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *current;
int i, j, check, *arr1, *arr2;
arr1 = malloc(sizeof(int) * list_len(*head));
arr2 = malloc(sizeof(int) * list_len(*head));
if (arr1 == NULL || arr2 == NULL)
return (0);
current = *head;
if (*head == NULL)
return (1);
i = 0;
while (current->next != NULL)
{
arr1[i] = current->n;
current = current->next;
i++;
}
arr1[i] = current->n;
j = 0;
while (i >= 0)
{
arr2[j] = arr1[i];
j++;
i--;
}
check = compare(arr1, arr2, j - 1);
if (check)
return (1);
return (0);
}

/**
 * compare - compares int elements of two arrays
 * @arr1: the first array
 * @arr2: the second array
 * @size: the array's size
 * Return: 1 if elements are same, 0 otherwise
 */
int compare(int *arr1, int *arr2, int size)
{
int is_true, i = 0;
while (size >= 0)
{
if (arr1[i] == arr2[i])
{
is_true = 1;
}
else
{
free(arr1);
free(arr2);
return (0);
}
size--;
i++;
}
free(arr1);
free(arr2);
return (is_true);
}

/**
 * list_len - returns the number of elements in a linked list_t list.
 *
 * @h: the head node
 *
 * Return: the number of elements in the node
 */
size_t list_len(listint_t *h)
{
size_t n = 0;
while (h != NULL)
{
h = h->next;
n++;
}
return (n);
}
