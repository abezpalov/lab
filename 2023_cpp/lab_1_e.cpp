#include <iostream>

using namespace std;

int main() {

    // Считываем дроби
    int q1, r1, q2, r2;
    cin >> q1 >> r1;
    cin >> q2 >> r2;

    // Считаем
    int p, q, r;
    r = r1 * r2;
    q = q1 * r2 + q2 * r1;

    p = q / r;
    q = q % r;

    cout << p << endl;
    cout << q << endl;
    cout << r << endl;

    return 0;
}
