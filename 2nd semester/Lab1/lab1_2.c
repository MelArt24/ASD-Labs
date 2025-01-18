// Код на рекурсивному поверненні

#include <stdio.h>

double RecursionPov(double x, unsigned int n, double* sum)
{
 double i = 0.0;
 if (n == 1)
   i = x;
 else
   i = ((x * x * (2 * (n - 1) - 1) * (2 * (n - 1) - 1)) / (4 * (n - 1) * (n - 1) + 2 * (n - 1))) * 
   RecursionPov(x, n - 1, sum);
   *sum += i;
 return i;
}

int main()
{
 double x;
 int n;
 printf("Enter the value of x (-1 < x < 1): ");
 scanf("%lf", &x);
 if(x <= 1 && x >= -1)
 {
   printf("Enter the value of n: ");
   scanf("%d", &n);
   double sum = 0.0;
   RecursionPov(x, n, &sum);
   printf("Sum: %f\n", sum);
 }
 else
   printf("Error! x > 1 or x < -1!");
 return 0;
}
