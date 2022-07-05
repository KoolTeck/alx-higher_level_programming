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
int i, j, check, arr1[1020], arr2[1020];
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
int compare(int arr1[], int arr2[], int size)
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
return (0);
}
size--;
i++;
}
return (is_true);
}
