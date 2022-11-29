#include <stdio.h>
#include <stdlib.h>

int hammingWeight(unsigned n)
{

    int count = 0;
    while (n)
    {
        n = n & (n - 1);
        count++;
    }
    return count;
}

int main()
{
    printf("%d\n", hammingWeight(00000000000000000000000000001011));
}