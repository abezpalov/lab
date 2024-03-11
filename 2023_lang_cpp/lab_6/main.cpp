#include <iostream>
#include <vector>

using namespace std;

// 14. Попытка записи в несуществующий файл.
int main() {

    vector <long long> x = {0, 1, 2, 42};

    x.resize(42, 42);


    unsigned long long s = 18446744073709551615;
    x.resize(s, s);

    return 0;
}
