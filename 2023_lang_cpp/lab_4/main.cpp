#include <iostream>
#include <exception>
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
    Point e0 = Point(0, 0, 0);
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

    // Создаём треугольники
    cout << "Triangle::Triangle()" << endl;
    Triangle t0 = Triangle();
    cout << endl;

    cout << "Triangle::Triangle(Point A, Point B, Point C)" << endl;
    Triangle t1 = Triangle(a1, a2, a3);
    Triangle t2 = Triangle(a1+a4, a2+a4, a3+a4);
    t1.print();
    t2.print();
    cout << endl;

    cout << "t1.get_perimeter() = "
    << t1.get_a_length() << " + " << t1.get_b_length() << " + " << t1.get_c_length()
    << " = " << t1.get_perimeter() << endl;

    cout << "t1.get_A_angle() = " << t1.get_A_angle() << endl;
    cout << "t1.get_B_angle() = " << t1.get_B_angle() << endl;
    cout << "t1.get_C_angle() = " << t1.get_C_angle() << endl;

    cout << "t1.get_A_height() = " << t1.get_A_height() << endl;
    cout << "t1.get_B_height() = " << t1.get_B_height() << endl;
    cout << "t1.get_C_height() = " << t1.get_C_height() << endl;

    cout << "t1.get_A_median() = " << t1.get_A_median() << endl;
    cout << "t1.get_B_median() = " << t1.get_B_median() << endl;
    cout << "t1.get_C_median() = " << t1.get_C_median() << endl;

    cout << "t1.get_A_bisector() = " << t1.get_A_bisector() << endl;
    cout << "t1.get_B_bisector() = " << t1.get_B_bisector() << endl;
    cout << "t1.get_C_bisector() = " << t1.get_C_bisector() << endl;
    cout << endl;

    cout << "Triangle::is_right()" << endl;
    t1.print();
    cout << "t1.is_right() = " << t1.is_right() << endl;
    Triangle t3 = Triangle(e0, e1*3, e2);
    t3.print();
    cout << "t3.is_right() = " << t3.is_right() << endl;
    cout << endl;

    cout << "Triangle::is_isosceles()" << endl;
    t1.print();
    cout << "t1.is_isosceles() = " << t1.is_isosceles() << endl;
    Triangle t4 = Triangle(e0, e1*3, e2*3);
    t4.print();
    cout << "t4.is_isosceles() = " << t4.is_isosceles() << endl;
    cout << endl;

    cout << "Triangle::is_equilateral()" << endl;
    t1.print();
    cout << "t1.is_equilateral() = " << t1.is_equilateral() << endl;
    Triangle t5 = Triangle(e1*3, e2*3, e3*3);
    t5.print();
    cout << "t5.is_equilateral() = " << t5.is_equilateral() << endl;
    cout << endl;

    cout << "First class test is ok?" << endl;
    cout << (t1 == t2) << endl;
    cout << (t1 != t5) << endl;
    cout << endl;

    cout << "TriangleIsosceles::TriangleIsosceles(Point A, Point B, Point C)" << endl;
    TriangleIsosceles ti1 = TriangleIsosceles(e0, e1, e2);
    ti1.print();
    cout << "ti1.is_isosceles() = " << ti1.is_isosceles() << endl;
    cout << "ti1.is_equilateral() = " << ti1.is_equilateral() << endl;

    try {
        TriangleIsosceles ti2 = TriangleIsosceles(a1, a2, a3);
    }
    catch (const exception& ex){
        cout << "Exception is intercepted!!" << endl << endl;
    }

    // TriangleIsosceles ti3 = TriangleIsosceles(a1, a2, a3);


    cout << endl;

    cout << "TriangleEquilateral::TriangleEquilateral(Point A, Point B, Point C)" << endl;
    TriangleEquilateral te1 = TriangleEquilateral(e1*42, e2*42, e3*42);
    te1.print();
    cout << "te1.is_isosceles() = " << te1.is_isosceles() << endl;
    cout << "te1.is_equilateral() = " << te1.is_equilateral() << endl;
    TriangleEquilateral te2 = TriangleEquilateral(a1, a2, a3);
    cout << endl;


    // Роняем программу, некоррктным создание равностороннего треугольника
    TriangleEquilateral te3 = TriangleEquilateral(a1, a2, a3*42);

    return 0;
}
