#include <iostream>

using namespace std;

int main() {


    long n, m, T, d;

    cin >> n >> m >> T >> d;

    long result = 0;

    long current_time;

    for (int i = 0; i < n; i++) {
        cin >> current_time;

        if (current_time < m) {
            m -= current_time;
            result++;
        } else {
            break;
        }

        if (current_time >= T) {
            m -= d;
        }
    }

    cout << result;

    return 0;
}
