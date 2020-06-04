#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
   double x, n, m, cnt = 0.0;
   int i;

   // Any input
   printf("Enter a number.\n");
   scanf("%lf", &n);
   x = n;
   m = sqrt(n);

   // Divide by 4 until n < 1
   while (n > 1) {
      n = n/4;
      cnt++;
   }

   double mysqrt = 1.0;
   double x1 = 1.0;

   // Power series to estimate sqare root, the Taylor Series
   // sqrt(x) = 1 + 1/2(x-1) - 1/4(x-1)^2/2! + 3/8(x-1)^3/3! - 15/16(x-1)^4/4!
   // sqrt(1-x) = 1 - x/2 + 1/4(x-1)^2/2! - 3/8(x-1)^3/3! + 15/16(x-1)^4/4!
   // sqrt(1-x) = 1 - x/2 - x^2/4 - ... -{1*3*5...(2n-3)x^n/2*n*n!

   for (i=1; i<=4; i++) {
      x1 = x1 * (((2 * i) - 3) * (1-n)) / (2 * i);
      mysqrt = mysqrt + x1;

   }
  
   // Add up the pieces
   float total, tmp=1;
   if (cnt)
      for(i=0; i<cnt; i++)
         tmp *= 2;
   total = mysqrt * tmp;

   printf("Library function, the square root of %.3lf is %.3lf\n", x, m);
   printf("Talor Series, the square root of %.3lf is %.3lf\n", x, total);

   return 0;
}
