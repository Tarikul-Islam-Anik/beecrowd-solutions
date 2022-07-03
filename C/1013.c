#include <stdio.h>

int main()
{
    int a, b, c, max;
    scanf("%d %d %d", &a, &b, &c);
    if (b > max)
        max = b;
    if (c > max)
        max = c;
    printf("%d eh o maior\n", max);
    return 0;
}