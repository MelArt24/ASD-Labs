#include <stdio.h>
#include <stdlib.h>
int findTheLeftmost(double *arr, int size, double target)
{
  int left = 0;
  int right = size - 1;
  int result = -1;
  
  while (left <= right)
  {
    int mid = (left + right) / 2;
    if (arr[mid] == target)
    {
      result = mid;
      right = mid - 1;
    }
    else if (arr[mid] < target)
    left = mid + 1;
    else right = mid - 1;
  }
  return result;
}

int main()
{
 double X;
 printf("Enter X: ");
 scanf("%lf", &X);
 int rows, cols;
 printf("Enter size of Matrix: ");
 scanf("%d %d", &rows, &cols);
 double A[rows][cols];
 if ((rows < 7 || rows>10) || (cols < 7 || cols>10))
 {
    printf("Unacceptable size of matrix");
    return -1;
 }
 printf("Enter elements of Matrix:\n");
  
 for(int i=0; i<rows; i++)
 {
   for(int j=0; j<cols; j++)
   {
     scanf("%lf", &A[i][j]);
   }
 }
 for(int k=0; k<cols; k++)
 {
 int resultOfRow = findTheLeftmost(&A[0][k], cols, X);
 int a;
 for (int j = 0; j < cols - 1; j++)
 {
   if (A[0][j] > A[0][j + 1])
   {
     printf("The first row is not in non-decreasing order\n");
     a=2;
     break;
   }
 }
   if(a==2)
   {
     break;
   }
   else
   {
     if (resultOfRow >= 0)
     {
       printf("%lf", X);
       printf(" is found in the first row on position [0][%d]\n", resultOfRow);
       break;
     }
     else
     {
       printf("%lf is not found in the first row\n", X);
       break;
     }
   }
 }
 int nonDecreasing = 1;
 for (int k = 0; k < rows - 1; k++)
 {
   if (A[k][cols - 1] > A[k + 1][cols - 1])
   {
     nonDecreasing = 0;
     break;
   }
 }
 if (!nonDecreasing)
 {
   printf("The last column is not in non-decreasing order.\n");
 }
 else
 {
   int found = 0;
   for (int k = 0; k < rows; k++)
   {
     if (A[k][cols - 1] == X)
     {
       printf("%lf is found in the last column on position [%d][%d]\n", X, k, cols - 1);
       found = 1;
       break;
     }
   }
   if (!found)
   {
     printf("%lf is not found in the last column\n", X);
   }
 }
 return 0;
}
