#include <iostream>
using namespace std;

int main()
{
    int item, qty1;
    float price1;
    cin >> item >> qty1 >> price1;
    int qty2;
    float price2;
    cin >> item >> qty2 >> price2;
    float total = (qty1 * price1) + (qty2 * price2);
    cout.precision(2);
    cout << fixed << "VALOR A PAGAR: R$ " << total << endl;
    return 0;
}