#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>

#include "Point.h"


// Реализация класса Точка

Point::Point() {
    this->x = 0.0;
    this->y = 0.0;
    this->z = 0.0;
}

Point::Point(double x, double y, double z) {
    this->x = x;
    this->y = y;
    this->z = z;
}

Point::~Point() {
    //dtor
}

std::string Point::str() const{
    std::string result;
    result =  "(" + this->get_x_str() + "; " + this->get_y_str() + "; " + this->get_z_str() + ")";
    return result;
}

void Point::print() const{
    std::cout << this->str() << std::endl;
}

double Point::norm() const {
    return pow(pow(this->x, 2) + pow(this->y, 2) + pow(this->z, 2), 0.5);
}

Point& Point::operator=(const Point& obj){
    if (this!=&obj){
        this->x = obj.x;
        this->y = obj.y;
        this->z = obj.z;
    }
    return *this;
}

Point Point::operator+(const Point& obj) const{
    Point result(this->x + obj.x, this->y + obj.y, this->z + obj.z);
    return result;
}

Point Point::operator-(const Point& obj) const{
    Point result(this->x - obj.x, this->y - obj.y, this->z - obj.z);
    return result;
}

Point Point::operator*(const float& x) const{
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

Point Point::operator*(const double& x) const{
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

Point Point::operator*(const int& x) const{
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

Point Point::operator*(const long long& x) const{
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

double Point::operator*(const Point& obj) const{
    return this->x * obj.x + this->y * obj.y + this->z * obj.z;
}

bool Point::operator==(const Point& obj)  const{
    return (this->x - obj.x < 0.000001 ) && (this->y - obj.y < 0.000001 ) && (this->y - obj.y < 0.000001 );
}

bool Point::operator!=(const Point& obj)  const{
    return (this->x - obj.x > 0.000001 ) || (this->y - obj.y > 0.000001 ) || (this->y - obj.y > 0.000001 );
}

std::string Point::get_x_str() const{
    std::ostringstream s;
    s << this->x;
    return s.str();
}

std::string Point::get_y_str() const{
    std::ostringstream s;
    s << this->y;
    return s.str();
}

std::string Point::get_z_str() const{
    std::ostringstream s;
    s << this->z;
    return s.str();
}


// Реализация класса Треугольник

Triangle::Triangle() {
    this->A = Point();
    this->B = Point();
    this->C = Point();
}

Triangle::Triangle(Point A, Point B, Point C){
    this->A = A;
    this->B = B;
    this->C = C;
}

Triangle::~Triangle() {
    //dtor
}

std::string Triangle::str() const{
    return "A" + this->A.str() + " B" + this->B.str() + " C" + this->C.str();
}

void Triangle::print() const{
    std::cout << this->str() << std::endl;
}

double Triangle::square() const{

    // Площадь треугольника равна половине скалярного произведения векторов, образованных любыми двумя векторами сторон
    Point x = this->A - this->B;
    Point y = this->A - this->C;

    return (x * y) / 2;
}

Point Triangle::get_a() const{
    return this->B - this->C;
}

Point Triangle::get_b() const{
    return this->A - this->C;
}

Point Triangle::get_c() const{
    return this->B - this->A;
}

double Triangle::get_a_length() const{
    Point x = this->get_a();
    return x.norm();
}

double Triangle::get_b_length() const{
    Point x = this->get_b();
    return x.norm();
}

double Triangle::get_c_length() const{
    Point x = this->get_c();
    return x.norm();
}

double Triangle::get_perimeter() const{
    Point a = this->get_a();
    Point b = this->get_b();
    Point c = this->get_c();
    return a.norm() + b.norm() + c.norm();
}

double Triangle::get_A_angle() const{
    Point b = this->get_b();
    Point c = this->get_c();
    return acos((b*c) / (b.norm()* c.norm()));
}

double Triangle::get_B_angle() const{
    Point a = this->get_a();
    Point c = this->get_c();
    return acos((a*c) / (a.norm()* c.norm()));
}

double Triangle::get_C_angle() const{
    Point b = this->get_b();
    Point a = this->get_a();
    return acos((b*a) / (b.norm()* a.norm()));
}

double Triangle::get_A_height() const{
    Point x = this->A - this->B;
    Point y = this->A - this->C;

    Point a = this->B - this->C;

    return (x*y)/a.norm();
}

double Triangle::get_B_height() const{
    Point x = this->A - this->B;
    Point y = this->A - this->C;

    Point b = this->A - this->C;

    return (x*y)/b.norm();
}

double Triangle::get_C_height() const{
    Point x = this->A - this->B;
    Point y = this->A - this->C;

    Point c = this->B - this->A;

    return (x*y)/c.norm();
}

// TODO Point Triangle::get_intersection_of_heights() const;

double Triangle::get_A_median() const {
    Point x = (this->B + this->C)*0.5;
    Point m = (this->A - x);
    return m.norm();
}

double Triangle::get_B_median() const {
    Point x = (this->A + this->C)*0.5;
    Point m = (this->B - x);
    return m.norm();
}

double Triangle::get_C_median() const {
    Point x = (this->A + this->B)*0.5;
    Point m = (this->C - x);
    return m.norm();
}

// TODO Point Triangle::get_intersection_of_medians() const;

double Triangle::get_A_bisector() const{
    Point AM = this->A + this->get_b() + this->get_c();
    Point m = AM - this->A;
    return m.norm();
}

double Triangle::get_B_bisector() const{
    Point BM = this->B + this->get_a() + this->get_c();
    Point m = BM - this->B;
    return m.norm();
}

double Triangle::get_C_bisector() const{
    Point CM = this->C + this->get_a() + this->get_b();
    Point m = CM - this->C;
    return m.norm();
}

// TODO Point Triangle::get_intersection_of_bisectors() const;

bool Triangle::is_right() const{
    return (abs(cos(this->get_A_angle())) < 0.000001 ||
            abs(cos(this->get_B_angle())) < 0.000001 ||
            abs(cos(this->get_C_angle())) < 0.000001 );
}

bool Triangle::is_isosceles() const{
    return (abs(this->get_a_length() - this->get_b_length()) < 0.000001 ||
            abs(this->get_c_length() - this->get_b_length()) < 0.000001 ||
            abs(this->get_c_length() - this->get_a_length()) < 0.000001);
}

bool Triangle::is_equilateral() const{
    return (abs(this->get_a_length() - this->get_b_length()) < 0.000001 &&
            abs(this->get_c_length() - this->get_a_length()) < 0.000001);
}


Triangle& Triangle::operator=(const Triangle& obj){
    if (this!=&obj){
        this->A = obj.A;
        this->B = obj.B;
        this->C = obj.C;
    }
    return *this;
}

bool Triangle::operator==(const Triangle& obj){
    return (abs(this->get_a_length() - obj.get_a_length()) < 0.000001 &&
            abs(this->get_b_length() - obj.get_b_length()) < 0.000001 &&
            abs(this->get_c_length() - obj.get_c_length()) < 0.000001 );
}

bool Triangle::operator!=(const Triangle& obj){
    return (abs(this->get_a_length() - obj.get_a_length()) > 0.000001 ||
            abs(this->get_b_length() - obj.get_b_length()) > 0.000001 ||
            abs(this->get_c_length() - obj.get_c_length()) > 0.000001 );
}

bool Triangle::is_likeness(const Triangle& obj) const{
    return (abs(this->get_A_angle() - obj.get_A_angle()) < 0.000001 &&
            abs(this->get_B_angle() - obj.get_B_angle()) < 0.000001 &&
            abs(this->get_C_angle() - obj.get_C_angle()) < 0.000001 );
}




// Реализация класса Равнобедренный треугольник

TriangleIsosceles::TriangleIsosceles(){
    this->A = Point();
    this->B = Point();
    this->C = Point();
}

TriangleIsosceles::TriangleIsosceles(Point A, Point B, Point C){
    Point a = B - C;
    Point b = A - C;
    Point c = A - B;
    if (abs(a.norm() - b.norm()) < 0.000001 || abs(c.norm() - b.norm()) < 0.000001 || abs(c.norm() - a.norm()) < 0.000001){
        this->A = A;
        this->B = B;
        this->C = C;
    } else {
            throw 1;
    }
}

TriangleIsosceles::~TriangleIsosceles() {
    //dtor
}

bool TriangleIsosceles::is_isosceles() const{
    return true;
}

// Реализация класса Равносторонний треугольник

TriangleEquilateral::TriangleEquilateral(){
    this->A = Point();
    this->B = Point();
    this->C = Point();
}

TriangleEquilateral::TriangleEquilateral(Point A, Point B, Point C){
    Point a = B - C;
    Point b = A - C;
    Point c = A - B;
    if (abs(a.norm() - b.norm()) < 0.000001 && abs(c.norm() - b.norm()) < 0.000001){
        this->A = A;
        this->B = B;
        this->C = C;
    } else {
            throw 1;
    }
}

TriangleEquilateral::~TriangleEquilateral() {
    //dtor
}

bool TriangleEquilateral::is_equilateral() const{
    return true;
}


/*













        // Проверка треугольников на подобие (в геометрическом смысле по трём углам)
        // Без перестановок


        // Установка координат вершин
        void set_A(const Point& obj);
        void set_B(const Point& obj);
        void set_C(const Point& obj);


*/






















