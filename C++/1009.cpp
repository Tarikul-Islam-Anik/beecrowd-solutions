#include <iostream>
using namespace std;

int main()
{
    char name[25];
    double salary;
    double sales;
    cin >> name >> salary >> sales;
    if (sales > 0)
    {
        cout.precision(2);
        cout << fixed << "TOTAL = R$ " << salary + (sales * 0.15) << endl;
    }
    else
    {
        cout.precision(2);
        cout << fixed << "TOTAL = R$ " << salary << endl;
    }

    return 0;
}