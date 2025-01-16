#include <stdio.h>
#include <stdlib.h>
int main()
{
 float x, y=0;
 printf("Input x: ");
 scanf("%f", &x);
 if (x <= -30)
 {
   y = (3 * x * x * x) / 4 - 5;
   printf("y=%f\n", y);
 }
 else
 {
   if (x > -15)
   {
     if (x <= 3)
     {
       y = 4 * x * x + 2;
       printf("y=%f\n", y);
     }
     else
     {
       if (x > 20)
       {
         y = (3 * x * x * x) / 4 - 5;
         printf("y=%f\n", y);
       }
       else
       { 
       printf("no value for x\n");
       }
     }
   }
   else
   {
     printf("no value for x\n");
   }
 }
 return 0;
}
