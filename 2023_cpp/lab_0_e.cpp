#include <iostream>

using namespace std;

int main() {

    int n;
    int prev;
    int current;
    int value;

    int max_value = 0;
    int max_number;

    cin >> n;

    cin >> current;

    for (int i; i < n; i++) {

        prev = current;

        if (i == n-1) {
            current = 0;

        } else {
            cin >> current;
        }

        value = prev - current;

        if (value > max_value){
            max_number = i+1;
            max_value = value;
        }

    }

    cout << max_number << endl;

    return 0;
}
