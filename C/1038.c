#include <stdio.h>

int main()
{
    float i1 = 4.00, i2 = 4.50, i3 = 5.00, i4 = 2.00, i5 = 1.50, total;
    int item, quantity;
    scanf("%d %d", &item, &quantity);
    switch (item)
    {
    case 1:
        total = i1 * quantity;
        break;
    case 2:
        total = i2 * quantity;
        break;
    case 3:
        total = i3 * quantity;
        break;
    case 4:
        total = i4 * quantity;
        break;
    case 5:
        total = i5 * quantity;
        break;
    default:
        total = 0;
        break;
    }
    printf("Total: R$ %.2f\n", total);

    return 0;
}