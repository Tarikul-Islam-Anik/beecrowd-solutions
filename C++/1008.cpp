#include <iostream>
using namespace std;

int main()
{
    int a, b;
    float c;
    cin >> a >> b >> c;
    cout << "NUMBER = " << a << endl;
    cout.precision(2);
    cout << fixed << "SALARY = U$ " << (b * c) << endl;
    return 0;
}