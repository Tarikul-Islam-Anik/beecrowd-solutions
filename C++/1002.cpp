#include <iostream>

using namespace std;

int main()
{
    double r, area;
    cin >> r;
    area = r * r * 3.14159;
    cout.precision(4);
    cout << fixed << area << endl;

    return 0;
}
