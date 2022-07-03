#include <stdio.h>

int main()
{
    int sec;
    scanf("%d", &sec);
    printf("%d:%d:%d\n", sec / 3600, (sec % 3600) / 60, sec % 60);
    return 0;
}