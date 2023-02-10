#include <iostream>

using namespace std;

int main() {

    int n;
    cin >> n;

    int * t = new int [n];
    for (int i=0; i<n; i++) {
        cin >> t[i];
    }

    for (int j = 0; j < n; j++) {

        int base = 1;
        int ostatok = 0;

        while (true) {
            ostatok = t[j] % 10;
            t[j] = t[j] / 10;
            if (ostatok + 1 > base) {
                base = ostatok + 1;
            }
            if (t[j] == 0){
                break;
            }
        }
        cout << base << endl;
    }
    return 0;
}
