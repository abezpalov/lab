#ifndef POINT_H
#define POINT_H


class Point {

    public:
        Point();
        Point(double x, double y, double z);
        virtual ~Point();

        // Отображение координат точки
        void print() const;

        // Норма вектора, проведённого от начала координат к точке
        double norm() const;

        // Присваивание
        Point& operator=(const Point& obj);

        // Сложение и вычитание (как векторов)
        Point operator+(const Point& obj);
        Point operator-(const Point& obj);

        // Умножение на число
        Point operator*(const float& x);
        Point operator*(const double& x);
        Point operator*(const int& x);
        Point operator*(const long long& x);

        // Скалярное произведение (как векторов)
        double operator*(const Point& obj);

        // Проверка на равенство / неравенство
        bool operator==(const Point& obj);
        bool operator!=(const Point& obj);

    protected:

    private:
        double x;
        double y;
        double z;

};


class Triangle {

    public:
        Triangle();
        Triangle(Point A, Point B, Point C);
        virtual ~Triangle();

        // Отображение координат вершин
        void print() const;

        // Площадь треугольника
        double square() const;

        // Присваивание
        Triangle& operator=(const Triangle& obj);

        // Проверка на равенство / неравенство
        bool operator==(const Point& obj);
        bool operator!=(const Point& obj);

        // Длина стороны, противоположная вершине
        float get_a_length() const;
        float get_b_length() const;
        float get_c_length() const;

        // Размер угла при соответствующей вершине (в медианах?)
        float get_A_angle() const;
        float get_B_angle() const;
        float get_C_angle() const;

        // Длина высоты, проведённой из соответствующей вершины
        float get_A_height() const;
        float get_B_height() const;
        float get_C_height() const;

        // Длина медианы, проведённой из соответствующей вершины
        float get_A_median() const;
        float get_B_median() const;
        float get_C_median() const;

        // Длина бисектрисы, проведённой из соответствующей вершины
        float get_A_bisector() const;
        float get_B_bisector() const;
        float get_C_bisector() const;

        // Прямоугольный треугольник?
        bool is_right() const;

        // Равнобедренный треугольник?
        bool is_isosceles() const;

        // Равносторонний треугольник?
        bool is_equilateral() const;




    protected:

    private:
        double x;
        double y;
        double z;



};




#endif // POINT_H
