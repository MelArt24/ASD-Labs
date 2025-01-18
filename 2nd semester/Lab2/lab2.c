#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
 int data;
 struct Node* next;
} Node;

Node* createNode(int data)
{
 Node* newNode = (Node*)malloc(sizeof(Node));
 if (newNode == NULL)
 {
   printf("Error allocating memory for node\n");
   exit(1);
 }
 newNode->data = data;
 newNode->next = NULL;
 return newNode;
}

void insertNode(Node** head, int data)
{
 Node* newNode = createNode(data);
 if (*head == NULL)
 {
   *head = newNode;
 }
 else
 {
   Node* temp = *head;
   while (temp->next != NULL)
   {
     temp = temp->next;
   }
   temp->next = newNode;
 }
}

void printList(Node* head)
{
 if (head == NULL)
 {
   printf("The list is empty\n");
   return;
 }
 while (head != NULL)
 {
   printf("%d ", head->data);
   head = head->next;
 }
 printf("\n");
}

void rearrangeList(Node** head)
{
 Node* positiveHead = NULL, * positiveTail = NULL;
 Node* zeroHead = NULL, * zeroTail = NULL;
 Node* negativeHead = NULL, * negativeTail = NULL;
 Node* curr = *head;
 while (curr != NULL)
 {
   Node* nextNode = curr->next;
   if (curr->data > 0)
   {
     if (positiveHead == NULL)
     {
       positiveHead = positiveTail = curr;
       positiveTail->next = NULL;
     }
     else
     {
       curr->next = positiveHead;
       positiveHead = curr;
     }
   }
   else if (curr->data == 0)
   {
     if (zeroHead == NULL)
     {
       zeroHead = zeroTail = curr;
       zeroTail->next = NULL;
     }
     else
     {
       curr->next = zeroHead;
       zeroHead = curr;
     }
   }
   else 
   {
     if (negativeHead == NULL)
     {
       negativeHead = negativeTail = curr;
       negativeTail->next = NULL;
     }
     else
     {
       curr->next = negativeHead;
       negativeHead = curr;
     }
   }
   curr = nextNode;
 }
 *head = positiveHead;
 if (zeroHead != NULL)
 {
   positiveTail->next = zeroHead;
   if (negativeHead != NULL)
   {
     zeroTail->next = negativeHead;
   }
 }
 else if (negativeHead != NULL)
 positiveTail->next = negativeHead;
}

void freeList(Node* head)
{
 while (head != NULL)
 {
   Node* temp = head;
   head = head->next;
   free(temp);
 }
}
int main()
{
 int n;
 printf("Enter number of elements: ");
 scanf("%d", &n);
 if (n <= 0)
 {
   printf("Number of the elements must be more than 0\n");
   return 1;
 }
 Node* head = NULL;
 printf("Enter %d elements in the list:\n", n);
 for (int i = 0; i < n; i++)
 {
   int data;
   scanf("%d", &data);
   insertNode(&head, data);
 }
 printf("Original List: \n");
 printList(head);
 rearrangeList(&head);
 printf("Rearranged List: \n");
 printList(head);
 freeList(head);
 return 0;
}
