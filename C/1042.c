#include <stdio.h>

int main()
{
    int lst[3], lst2[3];

    for (int i = 0; i < 3; i++)
    {
        scanf("%d", &lst[i]);
    }

    for (int i = 0; i < 3; i++)
    {
        lst2[i] = lst[i];
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = i + 1; j < 3; j++)
        {
            if (lst[i] > lst[j])
            {
                int temp = lst[i];
                lst[i] = lst[j];
                lst[j] = temp;
            }
        }
    }

    for (int i = 0; i < 3; i++)
    {
        printf("%d\n", lst[i]);
    }
    printf("\n");
    for (int i = 0; i < 3; i++)
    {
        printf("%d\n", lst2[i]);
    }

    return 0;
}