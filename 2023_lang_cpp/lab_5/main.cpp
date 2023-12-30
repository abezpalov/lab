#include <iostream>
#include <string>
#include <vector>

#include "Image.h"

using namespace std;

int main() {

    VectorImage v1 = VectorImage();
    v1.open("pikcha1.svg");
    v1.save("pikcha1_edited.svg");
    v1.close();

    VectorImage v2 = VectorImage("Point(0.0, 0.0, 0.0);");
    v2.save("pikcha2_new.svg");
    v2.close();

    cout << endl;

    BinaryImage b1 = BinaryImage();
    b1.open("photo1.png");
    b1.save("photo1_edited.png");
    b1.close();


    vector<long> data = {1, 2, 42};
    BinaryImage b2 = BinaryImage(data);
    b2.save("photo2_new.png");
    b2.close();

    cout << endl;


    // Демонстрируем полиморфизм
    Image &image1 = v1;
    image1.save("temp.tmp");

    Image &image2 = v2;
    image2.save("temp.tmp");

    Image &image3 = b1;
    image3.save("temp.tmp");

    Image &image4 = b2;
    image4.save("temp.tmp");






    return 0;
}
