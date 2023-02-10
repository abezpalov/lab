#include <iostream>

using namespace std;

int main()
{
    // Инициализируем переменные
    long a;
    long b;
    long c;
    long d;

    // Получаем значение переменных со стандартного потока ввода
    cin >> a >> b >> c >> d;

    // Проверяем условия и выводим результат
    if ((b + 2*c >= d) && (2*b + c >= a)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    
    return 0;

}
