#include <iostream>

using namespace std;

int main() {

    int n;
    int m;
    int t_j;

    int result = 1;

    cin >> n >> m;

    for (int i=0; i < m; i++) {
        cin >> t_j;
        result += t_j;
    }

    if (result > n) {
        cout << n << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}
