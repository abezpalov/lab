#include <iostream>
#include <math.h>

#include "Complex.h"

Complex::Complex(double _re, double _im){
    this->re = _re;
    this->im = _im;

    std::cout << "Создан объект Complex " << this->re << " + i*(" << this->im << ")" << std::endl;
};

Complex::~Complex(){
    std::cout << "Убит объект Complex" << std::endl;
};

double Complex::get_r(){
    double result;
    result = pow(pow(this->re, 2) + pow(this->im, 2), 0.5);
    return result;
};

double Complex::get_fi(){

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

double Complex::get_re(){
    return re;
};

double Complex::get_im(){
    return im;
};

void Complex::print(){
    std::cout << this->get_r() << "*exp(i*" << this->get_fi() << ")" << std::endl;
};

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






ComplexFrac::ComplexFrac(Complex _nominator, Complex _denominator){
    this->nominator = _nominator;
    this->denominator = _denominator;
    std::cout << "Создан объект ComplexFrac "
              << "( " << this->nominator.get_re() << " + i*(" << this->nominator.get_im() << ") )"
              << " / "
              << "( " << this->denominator.get_re() << " + i*(" << this->denominator.get_im() << ") )"
              << std::endl;

}







