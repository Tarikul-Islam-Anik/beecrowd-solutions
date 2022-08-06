#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        if (x >= 10 && x <= 20)
        {
            count++;
        }
    }
    cout << count << " in" << endl;
    cout << n - count << " out" << endl;
    return 0;
}