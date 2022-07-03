#include <stdio.h>
#include <math.h>
int main()
{
    int r;
    scanf("%d", &r);
    printf("VOLUME = %.3lf\n", (4.0 / 3.0) * 3.14159 * pow(r, 3));
    return 0;
}