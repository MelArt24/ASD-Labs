// Код на рекурсивному списку

#include <stdio.h>

double RecursionSpusk(double x, double n, int p, double* sum, double* F)
{
 double i = 0.0;
 if (n == 0)
 i = *sum;
 else if(n==1)
 return x;
 else
 {
   p++;
   *F = *F * (x * x * (2 * p - 1) * (2 * p - 1)) / (4 * p * p + 2 * p);
   *sum += *F;
   i = RecursionSpusk(x, n - 1, p, sum, F);
 }
 return i;
}

int main()
{
 double x;
 int n;
 int p = 0;
 printf("Enter the value of x (-1 < x < 1): ");
 scanf("%lf", &x);
 if(x >= -1 && x <= 1)
 {
   printf("Enter the value of n: ");
   scanf("%d", &n);
   double F = x;
   double sum = x;
   RecursionSpusk(x, n, p, &sum, &F);
   printf("Sum: %f\n", sum);
 }
 else
   printf("Error! x > 1 or x < -1!");
 return 0;
}
