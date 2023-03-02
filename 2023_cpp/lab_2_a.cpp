#include <iostream>

using namespace std;

int main() {

    // Считываем данные
    int x1, y1, x2, y2, w, h;
    cin >> x1 >> y1 >> x2 >> y2 >> w >> h;

    if ((x2 - x1 <= w) && (x2 - x1 >= -w) && (y2 - y1 <= h) && (y2 - y1 >= -h)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
