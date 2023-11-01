#include <iostream>
#include <math.h>

#include "Complex.h"

Complex::Complex(double _re, double _im){
    this->re = _re;
    this->im = _im;

    // std::cout << "Создан объект Complex " << this->re << " + i*(" << this->im << ")" << std::endl;
};

Complex::~Complex(){
    //std::cout << "Убит объект Complex" << std::endl;
};

void Complex::print() const{
    std::cout << this->get_r() << "*exp(i*" << this->get_fi() << ")" << std::endl;
};

double Complex::get_r() const{
    double result;
    result = pow(pow(this->re, 2) + pow(this->im, 2), 0.5);
    return result;
};

double Complex::get_fi() const{

    double fi;

    if (im ==  0.0){
        if (re >= 0.0){
            fi = 0.0;
        } else {
            fi = M_PI;
        }
    } else if (re == 0.0) {
        if (im > 0.0){
            fi = 0.5 * M_PI;
        } else {
            fi = 1.5 * M_PI;
        }
    } else {
        fi = atan(im / re);
        if (re < 0) {
            fi += M_PI;
        }
        if (fi < 0) {
            fi += 2 * M_PI;
        }
    }
    return fi;
};

double Complex::get_re() const{
    return re;
};

double Complex::get_im() const{
    return im;
};

Complex Complex::get_conjugated() const{
    Complex result(this->re, this->im * (-1));
    return result;
}

Complex& Complex::operator=(const Complex& c){
    if (this!=&c){
        this->re = c.re;
        this->im = c.im;
    }
    return *this;
}

Complex& Complex::operator=(const int& c){
    this->re = c;
    this->im = 0;
    return *this;
}

Complex& Complex::operator=(const long& c){
    this->re = c;
    this->im = 0;
    return *this;
}

Complex& Complex::operator=(const float& c){
    this->re = c;
    this->im = 0;
    return *this;
}

Complex& Complex::operator=(const double& c){
    this->re = c;
    this->im = 0;
    return *this;
}


Complex Complex::operator+(const Complex& c){
    Complex result(this->re + c.re, this->im + c.im);
    return result;
}

Complex Complex::operator+(const int& c){

    Complex result(this->re + c, this->im);
    return result;
}

Complex Complex::operator+(const long& c){

    Complex result(this->re + c, this->im);
    return result;
}

Complex Complex::operator+(const float& c){

    Complex result(this->re + c, this->im);
    return result;
}

Complex Complex::operator+(const double& c){

    Complex result(this->re + c, this->im);
    return result;
}


Complex Complex::operator-(const Complex& c){

    Complex result(this->re - c.re, this->im - c.im);
    return result;
}

Complex Complex::operator-(const int& c){

    Complex result(this->re - c, this->im);
    return result;
}

Complex Complex::operator-(const long& c){

    Complex result(this->re - c, this->im);
    return result;
}

Complex Complex::operator-(const float& c){

    Complex result(this->re - c, this->im);
    return result;
}

Complex Complex::operator-(const double& c){

    Complex result(this->re - c, this->im);
    return result;
}


Complex Complex::operator*(const Complex& c){

    Complex result(
                this->re * c.re - this->im * c.im,
                this->re * c.im + this->im * c.re);
    return result;
}

Complex Complex::operator*(const int& c){

    Complex result(
                this->re * c,
                this->im * c);
    return result;
}

Complex Complex::operator*(const long& c){

    Complex result(
                this->re * c,
                this->im * c);
    return result;
}

Complex Complex::operator*(const float& c){

    Complex result(
                this->re * c,
                this->im * c);
    return result;
}

Complex Complex::operator*(const double& c){

    Complex result(
                this->re * c,
                this->im * c);
    return result;
}


Complex Complex::operator/(const Complex& c){

    if (c.get_r()==0.0){
        throw;
    }

    Complex result(

                // a = this->re
                // b = this->im
                // c = c.re
                // d = c.im

                // (a*c + b*d) / (c**2 + d**2)
                (this->re * c.re + this->im * c.im)
                /
                (pow(c.re, 2) + pow(c.im, 2)),
                // (b*c - a*d) / (c**2 + d**2)
                (this->im * c.re - this->re * c.im)
                /
                (pow(c.re, 2) + pow(c.im, 2))
                );
    return result;
}

Complex Complex::operator/(const int& c){

    if (c==0){
        throw;
    }

    Complex result(this->re / c, this->im / c);
    return result;
}

Complex Complex::operator/(const long& c){

    if (c==0){
        throw;
    }

    Complex result(this->re / c, this->im / c);
    return result;
}

Complex Complex::operator/(const float& c){

    if (c==0.0){
        throw;
    }

    Complex result(this->re / c, this->im / c);
    return result;
}

Complex Complex::operator/(const double& c){

    if (c==0.0){
        throw;
    }

    Complex result(this->re / c, this->im / c);
    return result;
}

bool Complex::operator==(const Complex& c){

    const double accuracy = 0.000000001;

    if (
        (this->re >= c.re - accuracy) &&
        (this->im >= c.im - accuracy) &&
        (this->re <= c.re + accuracy) &&
        (this->im <= c.im - accuracy)
    ) {
        return true;
    } else {
        return false;
    }
}

bool Complex::operator!=(const Complex& c){

    const double accuracy = 0.000000001;

    if (
        (this->re >= c.re - accuracy) &
        (this->im >= c.im - accuracy) &
        (this->re <= c.re + accuracy) &
        (this->im <= c.im - accuracy)
    ) {
        return false;
    } else {
        return true;
    }
}

bool Complex::operator<(const Complex& c){
    return this->get_r() > c.get_r();
}

bool Complex::operator>(const Complex& c){
    return this->get_r() > c.get_r();
}

ComplexFrac::ComplexFrac(Complex _nominator, Complex _denominator){
    this->nominator = _nominator;
    this->denominator = _denominator;
    std::cout << "Создан объект ComplexFrac "
              << "( " << this->nominator.get_re() << " + i*(" << this->nominator.get_im() << ") )"
              << " / "
              << "( " << this->denominator.get_re() << " + i*(" << this->denominator.get_im() << ") )"
              << std::endl;

}










