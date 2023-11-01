#include <iostream>

#include "Complex.h"
#include "Conus.h"

using namespace std;


int main()
{
    setlocale(LC_ALL,"russian");

    cout << "Создаём и отображаем тестовые объекты!" << endl;
    Complex a(1.0, 0.0);
    Complex b(0.0, 1.0);
    Complex c(-1.0, 0.0);
    Complex d(0.0, -1.0);
    Complex e(1.0, 1.0);
    Complex f(0.0, 0.0);

    a.print();
    b.print();
    c.print();
    d.print();
    e.print();

    cout << "Проверяем присваивание!" << endl;
    f.print();
    f = a;
    f.print();

    cout << "Проверяем сложение!" << endl;
    f = a + a + a + a + b + 1 + 2.0;
    f.print();

    cout << "Проверяем вычитание!" << endl;
    f = a - b - b - b - b * a + b + 1 + 2.0;
    f.print();

    cout << "Проверяем расчёт сопряжённого!" << endl;
    e.print();
    e.get_conjugated().print();

    return 0;
}
