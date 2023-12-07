#include <iostream>

using namespace std;

int main() {

    // Считываем данные
    int h1, w1, l1, h2, w2, l2;
    cin >> h1 >> w1 >> l1 >> h2 >> w2 >> l2;

    int result = 0;

    if (h2 < h1 && w2 < w1 && l2 < l1) result = 2;
    if (h2 < h1 && w2 < l1 && l2 < w1) result = 2;

    if (h2 < w1 && w2 < l1 && l2 < h1) result = 2;
    if (h2 < w1 && w2 < h1 && l2 < l1) result = 2;

    if (h2 < l1 && w2 < h1 && l2 < w1) result = 2;
    if (h2 < l1 && w2 < w1 && l2 < h1) result = 2;

    if (h2 > h1 && w2 > w1 && l2 > l1) result = 1;
    if (h2 > h1 && w2 > l1 && l2 > w1) result = 1;

    if (h2 > w1 && w2 > l1 && l2 > h1) result = 1;
    if (h2 > w1 && w2 > h1 && l2 > l1) result = 1;

    if (h2 > l1 && w2 > h1 && l2 > w1) result = 1;
    if (h2 > l1 && w2 > w1 && l2 > h1) result = 1;


    cout << result << endl;

    return 0;
}
