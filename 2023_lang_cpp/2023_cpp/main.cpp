#include <iostream>
#include <fstream>

using namespace std;




int main() {

    fstream f1;
    fstream f2;

    f1.open("f1.txt", ios::out);
    f1 << "test";
    f1.close();

    f2.open("f2.txt", ios::out);
    f2 << "test";
    f2.close();




    return 0;
}
