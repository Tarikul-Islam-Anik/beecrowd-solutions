#include <stdio.h>
int main()
{
    float a,b,c;
    scanf("%f%f%f",&a,&b,&c);
    a *= 2;
    b *= 3;
    c *= 5;
    printf("MEDIA = %.1f\n",(a+b+c)/10);
    return 0;
}