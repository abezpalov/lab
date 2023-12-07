#include <iostream>
#include <cmath>

using namespace std;

int main() {

    // Начало чтения
    int h1, m1, s1;
    cin >> h1 >> m1 >> s1;

    // Конец чтения
    int h2, m2, s2;
    cin >> h2 >> m2 >> s2;

    // Считаем разницу
    int h, m, s;
    h = h2 - h1;
    m = m2 - m1;
    s = s2 - s1;

    // Приводим в соответствие диапазону
    if (s < 0) {
        m--;
        s += 60;
    } else if (s > 59) {
        m++;
        s -= 60;
    }

    if (m < 0) {
        h--;
        m += 60;
    } else if (m > 59) {
        h++;
        m -= 60;
    }

    if (h < 0) {
        h += 24;
    }

    cout << h << endl;
    cout << m << endl;
    cout << s << endl;

    return 0;
}
