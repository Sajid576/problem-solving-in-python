#include<stdio.h>

void foo(int i)
{
    if(i>1)
    {
        foo(i/2);
        foo(i/2);
    }
    printf("* \n");
}

/*
stack:  

ouptut: *******



*/
int main()
{
    foo(4);
}