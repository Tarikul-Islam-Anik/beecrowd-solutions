#include <iostream>
using namespace std;
int main()
{
    double x, y;
    cin >> x >> y;
    x *= 3.5;
    y *= 7.5;
    cout.precision(5);
    cout << fixed << "MEDIA = " << (x + y) / 11 << endl;
    return 0;
}