#include <iostream>
using namespace std;

int main()
{
    float a, b, c;
    cin >> a >> b >> c;
    if (a + b > c && a + c > b && b + c > a)
    {
        cout.precision(1);
        cout << fixed << "Perimetro = " << a + b + c << endl;
    }
    else
    {
        cout.precision(1);
        cout << fixed << "Area = " << ((a + b) * c) / 2 << endl;
    }
    return 0;
}