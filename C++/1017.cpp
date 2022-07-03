#include <iostream>
using namespace std;

int main()
{
    int hours, kilos;
    cin >> hours;
    cin >> kilos;
    cout.precision(3);
    cout << fixed << (kilos / 12.0) * hours << endl;
    return 0;
}