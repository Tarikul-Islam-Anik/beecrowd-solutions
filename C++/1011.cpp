#include <iostream>
using namespace std;

int main()
{
    int r;
    cin >> r;
    cout.precision(3);
    cout << fixed << "VOLUME = " << (4.0 / 3.0) * r * r * r * 3.14159 << endl;
    return 0;
}