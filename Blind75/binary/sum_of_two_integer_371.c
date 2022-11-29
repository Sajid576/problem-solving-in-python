
#include <stdio.h>
#include <stdlib.h>

int sum(int x, int y)
{
  while (y != 0)
  {
    unsigned carry = x & y; // used unsigned as it can store more bit on the positive side
    x = x ^ y;
    y = carry << 1;
  }
  return x;
}

int main()
{
  printf("%d\n", sum(12, -3));
}
