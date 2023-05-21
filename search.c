#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int numbers[] ={20, 500, 10, 5, 50, 100, 1};

    int n = get_int("Number: ");
    for(int i=0; i<7; i++)
    {
        if(numbers[i] == n)
        {
            printf("Found\n");
            return 0;
        }

    }
    printf("Not found\n");
    return 1;
}