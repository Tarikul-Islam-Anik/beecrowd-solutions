#include <stdio.h>

int main()
{
    int item, qty1;
    float price1;
    scanf("%d %d %f", &item, &qty1, &price1);
    int qty2;
    float price2;
    scanf("%d %d %f", &item, &qty2, &price2);
    float total = (qty1 * price1) + (qty2 * price2);
    printf("VALOR A PAGAR: R$ %.2f\n", total);
    return 0;
}