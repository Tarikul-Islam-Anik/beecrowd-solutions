#include <iostream>

using namespace std;

int main()
{
    double notes;
    cin >> notes;
    int x, y, z;
    x = notes;
    notes = 100 * notes;
    z = notes;
    cout << "NOTAS:" << endl;
    cout << x / 100 << " nota(s) de R$ 100.00" << endl;
    y = (x % 100);
    cout << y / 50 << " nota(s) de R$ 50.00" << endl;
    y = (y % 50);
    cout << y / 20 << " nota(s) de R$ 20.00" << endl;
    y = (y % 20);
    cout << y / 10 << " nota(s) de R$ 10.00" << endl;
    y = (y % 10);
    cout << y / 5 << " nota(s) de R$ 5.00" << endl;
    y = (y % 5);
    cout << y / 2 << " nota(s) de R$ 2.00" << endl;
    y = (y % 2);
    cout << "MOEDAS:" << endl;
    cout << y / 1 << " moeda(s) de R$ 1.00" << endl;
    z = z % 100;
    cout << z / 50 << " moeda(s) de R$ 0.50" << endl;
    z = z % 50;
    cout << z / 25 << " moeda(s) de R$ 0.25" << endl;
    z = z % 25;
    cout << z / 10 << " moeda(s) de R$ 0.10" << endl;
    z = z % 10;
    cout << z / 5 << " moeda(s) de R$ 0.05" << endl;
    z = z % 5;
    cout << z / 1 << " moeda(s) de R$ 0.01" << endl;

    return 0;
}