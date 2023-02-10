#include <iostream>

using namespace std;

int main() {

    int n;
    cin >> n;

    int zeroes = 0;
    int ones = 0;

    while (n) {
        if (n % 2) {
            ones++;
        } else {
            zeroes++;
        }
        n = n / 2;
    }

    cout << zeroes << endl;
    cout << ones << endl;


    return 0;
}
