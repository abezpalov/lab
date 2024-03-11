#ifndef POINT_H
#define POINT_H

#include <stdexcept>
#include <string>


class Point {

    public:
        Point();
        Point(double x, double y, double z);
        virtual ~Point();

        // Представление в строковый тип
        std::string str() const;

        // Отображение координат точки
        void print() const;

        // Норма вектора, проведённого от начала координат к точке
        double norm() const;

        // Присваивание
        Point& operator=(const Point& obj);

        // Сложение и вычитание (как векторов)
        Point operator+(const Point& obj) const;
        Point operator-(const Point& obj) const;

        // Умножение на число
        Point operator*(const float& x) const;
        Point operator*(const double& x) const;
        Point operator*(const int& x) const;
        Point operator*(const long long& x) const;

        // Скалярное произведение (как векторов)
        double operator*(const Point& obj) const;

        // Проверка на равенство / неравенство
        bool operator==(const Point& obj) const;
        bool operator!=(const Point& obj) const;

    protected:

    private:
        double x;
        double y;
        double z;

        std::string get_x_str() const;
        std::string get_y_str() const;
        std::string get_z_str() const;

};


class Triangle {

    public:
        Triangle();
        Triangle(Point A, Point B, Point C);
        virtual ~Triangle();

        // Представление в строковый тип
        std::string str() const;

        // Отображение координат вершин
        void print() const;

        // Площадь треугольника
        double square() const;

        // Стороны треугольника как векторы
        Point get_a() const;
        Point get_b() const;
        Point get_c() const;

        // Длина стороны, противоположной вершине
        double get_a_length() const;
        double get_b_length() const;
        double get_c_length() const;
        double get_perimeter() const;

        // Размер угла при соответствующей вершине (в медианах)
        double get_A_angle() const;
        double get_B_angle() const;
        double get_C_angle() const;

        // Длина высоты, проведённой из соответствующей вершины
        double get_A_height() const;
        double get_B_height() const;
        double get_C_height() const;
        Point get_intersection_of_heights() const;

        // Длина медианы, проведённой из соответствующей вершины
        double get_A_median() const;
        double get_B_median() const;
        double get_C_median() const;
        Point get_intersection_of_medians() const;

        // Длина бисектрисы, проведённой из соответствующей вершины
        double get_A_bisector() const;
        double get_B_bisector() const;
        double get_C_bisector() const;
        Point get_intersection_of_bisectors() const;

        // Прямоугольный треугольник?
        bool is_right() const;

        // Равнобедренный треугольник?
        bool is_isosceles() const;

        // Равносторонний треугольник?
        bool is_equilateral() const;

        // Присваивание
        Triangle& operator=(const Triangle& obj);

        // Проверка на равенство / неравенство (в геометрическом смысле по трём сторонам)
        // Без перестановок: ABC != BCA в общем случае
        bool operator==(const Triangle& obj);
        bool operator!=(const Triangle& obj);

        // Проверка треугольников на подобие (в геометрическом смысле по трём углам)
        // Без перестановок
        bool is_likeness(const Triangle& obj) const;

        // Установка координат вершин
        void set_A(const Point& obj);
        void set_B(const Point& obj);
        void set_C(const Point& obj);


    protected:
        Point A;
        Point B;
        Point C;

    private:

};


class TriangleIsoscelesCreateError: public std::invalid_argument {
    public:
        explicit TriangleIsoscelesCreateError(double _value):
            std::invalid_argument("Из заданных точек не создать равнобедренный треугольник. Отклонение = " + std::to_string(_value) ),
                                  value(_value ) {}
            double getValue() const { return value; }
    private:
        double value;
};


class TriangleIsosceles : public Triangle {

    public:
        TriangleIsosceles();
        TriangleIsosceles(Point A, Point B, Point C);
        virtual ~TriangleIsosceles();

        bool is_isosceles() const;

    protected:

    private:

};

class TriangleEquilateral : public TriangleIsosceles {

    public:
        TriangleEquilateral();
        TriangleEquilateral(Point A, Point B, Point C);
        virtual ~TriangleEquilateral();

        bool is_equilateral() const;

    protected:

    private:

};


#endif // POINT_H
