#ifndef COMPLEX_H
#define COMPLEX_H


class Complex {

private:

    double re; // Вещественная часть
    double im; // Мнимая часть

public:

    Complex(double _re=1.0, double _im=0.0);
    ~Complex();
    void print() const;
    double get_r() const; // Модуль комплексного числа числа
    double get_fi() const; // Угол поворота комплексного числа
    double get_re() const; // Вещественная часть
    double get_im() const; // Мнимая часть
    Complex get_conjugated() const; // Возвращает сопряжённое число

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

    // Проверка на равенство
    bool operator==(const Complex& c);
    bool operator!=(const Complex& c);

    // Сравнение по модулю!!
    bool operator<(const Complex& c);
    bool operator>(const Complex& c);

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
