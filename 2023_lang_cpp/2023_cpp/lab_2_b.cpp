#include <iostream>

using namespace std;

int main() {

    // Считываем данные
    int p1, p2, s1, s2, t1, t2;
    cin >> p1 >> p2 >> s1 >> s2 >> t1 >> t2;

    int time1 = 0;
    int time2 = 0;
    int time3 = 0;

    // Брутфорс оптимального маршрута
    if ((p2 >= s2) && (p2 >= t2)) {
        time1 = p1 + p2;
        if (s2 >= t2){
            time2 = p1 + s1 + s2;
            time3 = p1 + s1 + t1 + t2;
        } else {
            time2 = p1 + t1 + t2;
            time3 = p1 + t1 + s1 + s2;
        }

    } else if (s2 >= t2) {
        time1 = s1 + s2;
        if (p2 >= t2){
            time2 = s1 + p1 + p2;
            time3 = s1 + p1 + t1 + t2;
        } else {
            time2 = s1 + t1 + t2;
            time3 = s1 + t1 + p1 + p2;
        }

    } else {
        time1 = t1 + t2;
        if (p2 >= s2){
            time2 = t1 + p1 + p2;
            time3 = t1 + p1 + s1 + s2;
        } else {
            time2 = t1 + s1 + s2;
            time3 = t1 + s1 + p1 + p2;
        }
    }

    if ((time1 > time2) && (time1 > time3)) {
        cout << time1 << endl;
    } else if (time2 > time3) {
        cout << time2 << endl;
    } else {
        cout << time3 << endl;
    }




    return 0;
}
