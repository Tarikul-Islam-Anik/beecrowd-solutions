#include <iostream>
using namespace std;

int main()
{
    int x;
    cin >> x;
    float y;
    cin >> y;
    cout.precision(3);
    cout << fixed << x / y << " km/l" << endl;
    return 0;
}