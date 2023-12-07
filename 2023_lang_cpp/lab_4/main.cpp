#include <iostream>
#include "Point.h"

using namespace std;

int main() {

    // Создаём несколько точек
    cout << "Make some points." << endl;
    Point a0 = Point();
    Point a1 = Point(5, 9, 3);
    Point a2 = Point(8, 95, 65);
    Point a3 = Point(0, 12, 1);
    Point a4 = Point(2, 15, 25);

    // Отображаем точки
    a0.print();
    a1.print();
    a2.print();
    a3.print();
    a4.print();
    cout << endl;

    // Отображаем эвклидово расстояние до начала координат
    cout << "Point::norm()" << endl;
    cout << a0.norm() << endl;
    cout << a1.norm() << endl;
    cout << a2.norm() << endl;
    cout << a3.norm() << endl;
    cout << a4.norm() << endl;
    cout << endl;

    // Поиграем с базисом
    cout << "{e1, e2, s3} = " << endl;
    Point e1 = Point(1, 0, 0);
    Point e2 = Point(0, 1, 0);
    Point e3 = Point(0, 0, 1);
    e1.print();
    e2.print();
    e3.print();
    cout << endl;

    Point r1;
    cout << "Point::Point()" << endl;
    r1.print();
    cout << endl;

    cout << "e1 * 20.5 + e2 * 10.9 + e3 * -56.3 = " << endl;
    r1 =  e1 * 20.5 + e2 * 10.9 + e3 * -56.3;
    r1.print();
    cout << endl;






    return 0;
}
