#include <iostream>
#include <list>
using namespace std;

int main()
{
    list<int> numbers, numbers_sorted ;
    int n1, n2, n3;
    cin >> n1 >> n2 >> n3;
    numbers.push_back(n1);
    numbers.push_back(n2);
    numbers.push_back(n3);
    for (list<int>::iterator it = numbers.begin(); it != numbers.end(); it++)
    {
        numbers_sorted.push_back(*it);
    }
    numbers_sorted.sort();
    for (list<int>::iterator it = numbers_sorted.begin(); it != numbers_sorted.end(); it++)
    {
        cout << *it << endl;
    }
    cout << endl;
    for (list<int>::iterator it = numbers.begin(); it != numbers.end(); it++)
    {
        cout << *it << endl;
    }
    return 0;
}