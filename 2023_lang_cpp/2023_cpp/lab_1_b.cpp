#include <iostream>

using namespace std;

int main() {

    int n, p, k;

    cin >> n;
    cin >> p >> k;

    int ostatok, izlishek;

    ostatok = (p * k) % n;
    cout << ostatok << endl;

    izlishek = ostatok / k;
    cout << izlishek << endl;

    return 0;
}
