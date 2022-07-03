#include <stdio.h>

int main()
{
    int notes, hundred, fifty, twenty, ten, five, two, one;
    scanf("%d", &notes);
    printf("%d\n", notes);
    hundred = notes / 100;
    notes = notes % 100;
    printf("%d nota(s) de R$ 100,00\n", hundred);
    fifty = notes / 50;
    notes = notes % 50;
    printf("%d nota(s) de R$ 50,00\n", fifty);
    twenty = notes / 20;
    notes = notes % 20;
    printf("%d nota(s) de R$ 20,00\n", twenty);
    ten = notes / 10;
    notes = notes % 10;
    printf("%d nota(s) de R$ 10,00\n", ten);
    five = notes / 5;
    notes = notes % 5;
    printf("%d nota(s) de R$ 5,00\n", five);
    two = notes / 2;
    notes = notes % 2;
    printf("%d nota(s) de R$ 2,00\n", two);
    one = notes;
    printf("%d nota(s) de R$ 1,00\n", one);

    return 0;
}