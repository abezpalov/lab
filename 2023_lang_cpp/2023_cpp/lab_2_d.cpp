#include <iostream>

using namespace std;

int main() {

    // Считываем данные
    long long w, h, s;
    cin >> w >> h >> s;

    // Считаем, сколько целых секций уйдёт на забор
    long result = 0;

    result += (w / s) * 2;
    result += (h / s) * 2;

    // Считаем остаток
    w = w % s;
    h = h % s;

    if (w==0 && h==0) { // Достаивать не нужно
        ;

    } else if (w==0) { // Нужно достоить только короткую сторону
        if (h <= s/2) {
            result ++;
        } else {
            result += 2;
        }

    } else if (h==0) { // Нужно достроить только длинную сторону
        if (w <= s/2) {
            result ++;
        } else {
            result += 2;
        }

    } else if (w + h <= s) { // Одной секции хватит на остаток длинной и короткой сторон
        result += 2;

    } else if (w < h ) {
        if (w <= s/2) {
            result++;
            if (h <= s/2){
                result++;
            } else {
                result += 2;
            }
        } else {
            result += 2;
            h = h - (s - w);
            if (h <= s/2){
                result++;
            } else {
                result += 2;
            }
        }
    } else {
        if (h <= s/2) {
            result++;
            if (w <= s/2){
                result++;
            } else {
                result += 2;
            }
        } else {
            result += 2;
            w = w - (s - h);
            if (w <= s/2){
                result++;
            } else {
                result += 2;
            }
        }
    }

    cout << result << endl;

    return 0;
}
