#include <iostream>

using namespace std;

int main() {

    int n, h;
    cin >> n >> h;

    int *hs = new int[n];
    for (int i=0; i < n; i++) {
        cin >> hs[i];
    }

    int best_h = 0;
    int best_delta = hs[0];
    int delta;

    for (int i=0; i < n; i++) {
        if (hs[i] > h) {
            delta = hs[i] - h;
        } else {
            delta = h - hs[i];
        }

        // cout << hs[i] << ' ' << delta << endl;

        if ( (delta < best_delta) || (delta == best_delta && hs[i] > best_h) ){
            best_delta = delta;
            best_h = hs[i];
        }
    }

    cout << best_h << endl;

    return 0;
}
