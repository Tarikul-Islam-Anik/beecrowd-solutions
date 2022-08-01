#include <iostream>
using namespace std;

int main()
{
    float n1, n2, n3, n4, n5, avg;
    cin >> n1 >> n2 >> n3 >> n4;
    avg = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10;
    cout.precision(1);
    cout << fixed << "Media: " << avg << endl;
    if (avg >= 7)
    {
        cout << "Aluno aprovado." << endl;
    }
    else if (avg >= 5)
    {
        cout << "Aluno em exame." << endl;
        cin >> n5;
        cout << "Nota do exame: " << n5 << endl;
        cout << "Aluno aprovado." << endl;
        cout << "Media final: " << (avg + n5) / 2 << endl;
    }
    else if (avg < 5)
    {
        cout << "Aluno reprovado." << endl;
    }

    return 0;
}