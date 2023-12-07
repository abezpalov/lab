#include <iostream>

using namespace std;

int main() {

    int w, h;
    cin >> w >> h;

    int razmer = 0;
    int result = 0;


    while (w != 0 && h != 0) {
        if (w >= h) {
            w -= h;
            if (razmer != h) {
                result++;
            }
            razmer = h;
        } else {
            h -= w;
            if (razmer != w) {
                result++;
            }
            razmer = w;
        }

    }

    cout << result << endl;

    return 0;
}
