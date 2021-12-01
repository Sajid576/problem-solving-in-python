using System;
class HelloWorld
{
    static void Main()
    {
        int decre = 1;
        int incre = 0;
        int i = 10;

        while (true)
        {
            Console.WriteLine(i);
            if (i == 1)
            {
                incre = 1;
                decre = 0;
            }
            if (decre == 1)
            {
                i--;
            }
            else if (incre == 1)
            {
                i++;
            }
            if (i == 11)
            {
                break;
            }
        }



    }
}