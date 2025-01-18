#include <stdio.h>
#include <math.h>
int main()
{
 int count=0;
 int n;
 double num, P = 1.0;
 scanf("%d", &n);
 for (int i = 1; i <= n; i++)
 {
   num = cos(i) + 1.0;
   count += 5;
   double denom = 0.0;
   for (int j = 1; j <= i; j++)
   {
     denom += sin(j);
     count+=5;
   }
   count+=2;
   P = P * (num / denom);
   count+=2;
 }
 count+=2;
 printf("%.7lf\n", P);
 printf("%d", count);
 return 0;
}
