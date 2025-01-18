#include <stdio.h>
#include <stdlib.h>

void sortMainDiagonal(int n, int matrix[n][n])
{
 int L = 0, R = n - 1, F = 1;
 int T;
 while (L < R && F == 1)
 {
   F = 0;
   for (int i = L; i < R; i++)
   {
     if (matrix[i][i] < matrix[i + 1][i + 1])
     {
       T = matrix[i][i];
       matrix[i][i] = matrix[i + 1][i + 1];
       matrix[i + 1][i + 1] = T;
       F = 1;
     }
   }
   R--;
   for (int i = R; i > L; i--)
   {
     if (matrix[i - 1][i - 1] < matrix[i][i])
     {
       T = matrix[i][i];
       matrix[i][i] = matrix[i - 1][i - 1];
       matrix[i - 1][i - 1] = T;
       F = 1;
     }
   }
   L++;
 }
}


int main()
{
 int n;
 printf("Enter n: ");
 scanf("%d", &n);
 int A[n][n];
 if(n<7 || n>10)
 {
   printf("Size of Matrix is unacceptable");
   return -1;
 }
 else
 {
   printf("Enter elements of Matrix: \n");
   for(int i=0; i<n; i++)
   {
     for(int j=0; j<n; j++)
     {
       scanf("%d", &A[i][j]);
     }
   }
   printf("Matrix before sort: \n");
   for (int i = 0; i < n; i++)
   {
     for (int j = 0; j < n; j++)
     {
       printf("%d ", A[i][j]);
     }
     printf("\n");
   }
   sortMainDiagonal(n, A);
   printf("Matrix after sort: \n");
   for (int i = 0; i < n; i++)
   {
     for (int j = 0; j < n; j++)
     {
       printf("%d ", A[i][j]);
     }
     printf("\n");
   }
 }
 return 0;
}
