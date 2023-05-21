#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string names[] = {"Hung" , "Ngoc"};
    string numbers[] = {"+84-58-997-7004" , "+84-33-723-6767"};

    string name = get_string("Name: ");
    for ( int i = 0 ; i < 2 ; i++)
    {
        if(strcmp(names[i], name) == 0 )
        //strcmp là hàm so sánh string ở thư viện string.h
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}