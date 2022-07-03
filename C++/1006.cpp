#include <iostream>
using namespace std;
int main()
{
    float a, b, c;
    cin >> a >> b >> c;
    a *= 2;
    b *= 3;
    c *= 5;
    cout.precision(1);
    cout << fixed << "MEDIA = " << (a + b + c) / 10 << endl;
    return 0;
}