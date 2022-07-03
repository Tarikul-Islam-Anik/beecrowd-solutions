#include <stdio.h>

int main()
{
    int hours, kilos;
    scanf("%d\n%d", &hours, &kilos);
    printf("%.3f\n", (kilos / 12.0) * hours);
    return 0;
}