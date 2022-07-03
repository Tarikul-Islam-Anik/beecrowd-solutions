#include <stdio.h>

int main()
{
    char name[25];
    double salary;
    double sales;

    scanf("%s %lf %lf", name, &salary, &sales);

    if (sales > 0)
    {
        printf("TOTAL = R$ %.2lf\n", (salary + (sales * 0.15)));
    }
    else
    {
        printf("TOTAL = R$ %.2lf\n", salary);
    }

    return 0;
}