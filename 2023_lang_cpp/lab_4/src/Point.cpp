#include <iostream>
#include <math.h>

#include "Point.h"

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

void Point::print() const{
    std::cout << "(" << this->x << "; " << this->y << "; " << this->z << ")" << std::endl;
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

Point Point::operator+(const Point& obj){
    Point result(this->x + obj.x, this->y + obj.y, this->z + obj.z);
    return result;
}

Point Point::operator-(const Point& obj){
    Point result(this->x - obj.x, this->y - obj.y, this->z - obj.z);
    return result;
}

Point Point::operator*(const float& x){
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

Point Point::operator*(const double& x){
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

Point Point::operator*(const int& x){
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

Point Point::operator*(const long long& x){
    Point result(this->x * x, this->y * x, this->z * x);
    return result;
}

double Point::operator*(const Point& obj){
    return this->x * obj.x + this->y * obj.y + this->z * obj.z;
}

bool Point::operator==(const Point& obj) {
    return (this->x - obj.x < 0.000001 ) && (this->y - obj.y < 0.000001 ) && (this->y - obj.y < 0.000001 );
}

bool Point::operator!=(const Point& obj) {
    return (this->x - obj.x > 0.000001 ) || (this->y - obj.y > 0.000001 ) || (this->y - obj.y > 0.000001 );
}




























