#ifndef COMPLEX_H
#define COMPLEX_H


class Complex {

private:

    double re; // Вещественная часть
    double im; // Мнимая часть

public:

    Complex(double _re=1.0, double _im=1.0);
    ~Complex();
    void print();

    Complex& operator=(const Complex& c);
    Complex& operator=(const int& c);
    Complex& operator=(const long& c);
    Complex& operator=(const float& c);
    Complex& operator=(const double& c);

    Complex operator+(const Complex& c);
    Complex operator+(const int& c);
    Complex operator+(const long& c);
    Complex operator+(const float& c);
    Complex operator+(const double& c);

    Complex operator-(const Complex& c);
    Complex operator-(const int& c);
    Complex operator-(const long& c);
    Complex operator-(const float& c);
    Complex operator-(const double& c);

    Complex operator*(const Complex& c);
    Complex operator*(const int& c);
    Complex operator*(const long& c);
    Complex operator*(const float& c);
    Complex operator*(const double& c);

    Complex operator/(const Complex& c);
    Complex operator/(const int& c);
    Complex operator/(const long& c);
    Complex operator/(const float& c);
    Complex operator/(const double& c);

    double get_r(); // Модуль комплексного числа числа
    double get_fi(); // Угол поворота комплексного числа

    double get_re(); // Вещественная часть
    double get_im(); // Мнимая часть

    Complex get_conjugated(); // Возвращает сопряжённое число

};

class ComplexFrac {

private:

    Complex nominator; // Числитель
    Complex denominator; // Знаменатель

public:

    ComplexFrac(Complex _nominator, Complex _denominator);
    ~ComplexFrac();
    void print();
    ComplexFrac& operator=(const ComplexFrac& c);

    ComplexFrac operator+(const ComplexFrac& c);

    ComplexFrac operator-(const ComplexFrac& c);
    ComplexFrac operator*(const ComplexFrac& c);
    ComplexFrac operator/(const ComplexFrac& c);
};







#endif // COMPLEX_H
