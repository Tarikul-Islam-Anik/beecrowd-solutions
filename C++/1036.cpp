#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float a, b, c;
    cin >> a >> b >> c;
    float delta = (b * b) - (4 * a * c);

    if ((delta < 0) || (a == 0))
    {
        cout << ("Impossivel calcular") << endl;
    }
    else
    {
        float x1 = (-b + sqrt(delta)) / (2 * a);
        float x2 = (-b - sqrt(delta)) / (2 * a);
        cout.precision(5);
        cout << fixed << ("R1 = ") << x1 << endl;
        cout.precision(5);
        cout << fixed << ("R2 = ") << x2 << endl;
    }
    return 0;
}