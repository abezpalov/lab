#include <iostream>
#include <cmath>

using namespace std;

int main() {

    // Считываем данные
    double z, m, q;
    cin >> z;
    cin >> m >> q;

    // Считаем
    double result;
    result = m * q / (2 * z * 100);

    printf("%.6f", result);

    return 0;
}
