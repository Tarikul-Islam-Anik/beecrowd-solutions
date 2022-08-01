#include <iostream>
#include <map>
using namespace std;

int main()
{
    int x, y;
    map<int, float> menu;

    menu = {
        {1, 4.00},
        {2, 4.50},
        {3, 5.00},
        {4, 2.00},
        {5, 1.50}};
    cin >> x >> y;
    cout.precision(2);
    cout << fixed << "Total: R$ " << menu[x] * y << endl;
    return 0;
}