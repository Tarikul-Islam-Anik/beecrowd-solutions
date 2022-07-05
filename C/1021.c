#include <stdio.h>

int main()
{
    float notes;
    scanf("%f", &notes);
    int x, y, z;
    x = notes;
    notes = notes * 100;
    z = notes;
    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", x / 100);
    y = (x % 100);
    printf("%d nota(s) de R$ 50.00\n", y / 50);
    y = (y % 50);
    printf("%d nota(s) de R$ 20.00\n", y / 20);
    y = (y % 20);
    printf("%d nota(s) de R$ 10.00\n", y / 10);
    y = (y % 10);
    printf("%d nota(s) de R$ 5.00\n", y / 5);
    y = (y % 5);
    printf("%d nota(s) de R$ 2.00\n", y / 2);
    y = (y % 2);
    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", y / 1);
    z = z % 100;
    printf("%d moeda(s) de R$ 0.50\n", z / 50);
    z = z % 50;
    printf("%d moeda(s) de R$ 0.25\n", z / 25);
    z = z % 25;
    printf("%d moeda(s) de R$ 0.10\n", z / 10);
    z = z % 10;
    printf("%d moeda(s) de R$ 0.05\n", z / 5);
    z = z % 5;
    printf("%d moeda(s) de R$ 0.01\n", z / 1);
    return 0;
}