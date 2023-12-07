#include <iostream>

using namespace std;

int main() {

    // Считываем данные
    long num_of_alg_works, num_of_geom_works;
    long num_of_ambi, num_of_alg, num_of_geom;
    cin >> num_of_alg_works >> num_of_geom_works;
    cin >> num_of_ambi >> num_of_alg >> num_of_geom;

    // Результат
    long done = 0;
    long other = 0;
    long delta;


    // Помогаем с алгеброй силами алгебристов
    if (num_of_alg_works <= num_of_alg) {
        done += num_of_alg_works;
        num_of_alg_works = 0;
    } else {
        done += num_of_alg;
        num_of_alg_works -= num_of_alg;
    }

    // Помогаем с геометрией силами геометриков
    if (num_of_geom_works <= num_of_geom) {
        done += num_of_geom_works;
        num_of_geom_works = 0;
    } else {
        done += num_of_geom;
        num_of_geom_works -= num_of_geom;
    }

    if (num_of_geom_works > num_of_alg_works) {
        delta = num_of_geom_works - num_of_alg_works;
        if (delta <= num_of_ambi) {
            done += delta;
            num_of_geom_works -= delta;
            num_of_ambi -= delta;
        } else {
            done += num_of_ambi;
            num_of_geom_works -= num_of_ambi;
            num_of_ambi = 0;
        }
    } else if (num_of_geom_works < num_of_alg_works) {
        delta = num_of_alg_works - num_of_geom_works;
        if (delta <= num_of_ambi) {
            done += delta;
            num_of_alg_works -= delta;
            num_of_ambi -= delta;
        } else {
            done += num_of_ambi;
            num_of_alg_works -= num_of_ambi;
            num_of_ambi =0;
        }
    }

    if (num_of_ambi >= num_of_alg_works + num_of_geom_works){
        done += num_of_alg_works + num_of_geom_works;
        num_of_alg_works = 0;
        num_of_geom_works = 0;
    } else {
        done += num_of_ambi;
        num_of_alg_works -= num_of_ambi / 2;
        num_of_geom_works -= num_of_ambi / 2;
        num_of_alg_works -= num_of_ambi % 2;
    }

    if (num_of_alg_works > num_of_geom_works) {
        other = num_of_alg_works;
    } else {
        other = num_of_geom_works;
    }

    cout << done << endl;
    cout << other << endl;

    return 0;
}
