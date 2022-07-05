#include <stdio.h>
#include <math.h>
int main()
{
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    float delta = (b * b) - (4 * a * c);
    if ((delta < 0) || (a == 0))
    {
        printf("Impossivel calcular\n");
    }
    else
    {
        float x1 = (-b + sqrt(delta)) / (2 * a);
        float x2 = (-b - sqrt(delta)) / (2 * a);
        printf("R1 = %.5f\n", x1);
        printf("R2 = %.5f\n", x2);
    }
    return 0;
}