#include <iostream>
using namespace std;

int main()
{
    int sec;
    cin >> sec;
    int h = sec / 3600;
    sec = sec % 3600;
    int m = sec / 60;
    sec = sec % 60;
    int s = sec;
    cout << h << ":" << m << ":" << s << endl;
    return 0;
}