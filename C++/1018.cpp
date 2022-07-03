#include <iostream>
using namespace std;

int main()
{
    int notes, hundred, fifty, twenty, ten, five, two, one;
    cin >> notes;
    cout << notes << endl;
    hundred = notes / 100;
    notes = notes % 100;
    fifty = notes / 50;
    notes = notes % 50;
    twenty = notes / 20;
    notes = notes % 20;
    ten = notes / 10;
    notes = notes % 10;
    five = notes / 5;
    notes = notes % 5;
    two = notes / 2;
    notes = notes % 2;
    one = notes;
    cout << hundred << " nota(s) de R$ 100,00" << endl;
    cout << fifty << " nota(s) de R$ 50,00" << endl;
    cout << twenty << " nota(s) de R$ 20,00" << endl;
    cout << ten << " nota(s) de R$ 10,00" << endl;
    cout << five << " nota(s) de R$ 5,00" << endl;
    cout << two << " nota(s) de R$ 2,00" << endl;
    cout << one << " nota(s) de R$ 1,00" << endl;

    return 0;
}