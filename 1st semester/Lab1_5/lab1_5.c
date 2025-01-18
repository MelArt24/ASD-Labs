#include <stdio.h>
#include <float.h>
int main()
{
  int n;
  printf("Enter size of matrix (n X n) : ", n);
  scanf("%d", &n);
  if (n < 7 || n > 10)
  {
     printf("Unacceptable size of matrix\n");
     return 1;
  }
  double A[n][n];
  printf("Enter matrix A: \n");
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      scanf("%lf", &A[i][j]);
    }
  }
  double min_elem = -DBL_MAX;
  double max_elem = DBL_MAX;
  int min_i, max_i;
  for (int i = 0; i < n; i++)
  {
    if (A[i][i] < max_elem)
    {
      max_elem = A[i][i];
      max_i = i;
    }
    if (A[i][i] >= min_elem)
    {
      min_elem = A[i][i];
      min_i = i;
    }
  }
  double temp = A[min_i][min_i];
  A[min_i][min_i] = A[max_i][max_i];
  A[max_i][max_i] = temp;
  printf("New matrix:\n");
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
       printf("%lf", A[i][j]);
       printf(" ");
    }
    printf("\n");
  }
  return 0;
}
