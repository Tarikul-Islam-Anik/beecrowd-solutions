#include <stdio.h>
int main()
{
    double x, y;
    scanf("%lf%lf", &x, &y);
    x *= 3.5;
    y *= 7.5;
    printf("MEDIA = %.5lf\n", (x + y) / 11);

    return 0;
}