#include <stdio.h>

int main()
{
    int days;
    scanf("%d", &days);
    printf("%d ano(s)\n", days / 365);
    printf("%d mes(es)\n", (days % 365) / 30);
    printf("%d dia(s)\n", (days % 365) % 30);

    return 0;
}