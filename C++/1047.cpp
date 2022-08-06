#include <iostream>
using namespace std;

int main()
{
    int h1, h2, m1, m2, hour_difference, minute_difference;
    cin >> h1 >> m1 >> h2 >> m2;
    if ((h2 > h1) || ((h2 == h1) && (m2 > m1)))
    {
        hour_difference = h2 - h1;
    }
    else
    {
        hour_difference = (h2 - h1) + 24;
    }
    if (m2 < m1)
    {
        hour_difference -= 1;
        minute_difference = (m2 - m1) + 60;
    }
    else
    {
        minute_difference = m2 - m1;
    }
    cout << "O JOGO DUROU " << hour_difference << " HORA(S) E " << minute_difference << " MINUTO(S)" << endl;

    return 0;
}