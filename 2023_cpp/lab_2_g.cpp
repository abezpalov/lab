#include <iostream>
#include <string>

using namespace std;

bool is_diag(int x, int y, int x_, int y_) {

    if (x - x_ == y - y_ || x - x_ == y_ - y) {
        return true;
    }
    return false;
}

bool is_prime(int x, int y, int x_, int y_) {

    if (x == x_ || y == y_) {
        return true;
    }
    return false;
}



int main() {

    string fig;
    string fig_xy;
    string pole_xy;

    cin >> fig;
    cin >> fig_xy;
    cin >> pole_xy;

    int fig_x, fig_y;
    int pole_x, pole_y;

    switch (fig_xy[0]){
    case 'a':
        fig_x = 1;
        break;
    case 'b':
        fig_x = 2;
        break;
    case 'c':
        fig_x = 3;
        break;
    case 'd':
        fig_x = 4;
        break;
    case 'e':
        fig_x = 5;
        break;
    case 'f':
        fig_x = 6;
        break;
    case 'g':
        fig_x = 7;
        break;
    case 'h':
        fig_x = 8;
        break;
    }

    switch (fig_xy[1]){
    case '1':
        fig_y = 1;
        break;
    case '2':
        fig_y = 2;
        break;
    case '3':
        fig_y = 3;
        break;
    case '4':
        fig_y = 4;
        break;
    case '5':
        fig_y = 5;
        break;
    case '6':
        fig_y = 6;
        break;
    case '7':
        fig_y = 7;
        break;
    case '8':
        fig_y = 8;
        break;
    }

    switch (pole_xy[0]){
    case 'a':
        pole_x = 1;
        break;
    case 'b':
        pole_x = 2;
        break;
    case 'c':
        pole_x = 3;
        break;
    case 'd':
        pole_x = 4;
        break;
    case 'e':
        pole_x = 5;
        break;
    case 'f':
        pole_x = 6;
        break;
    case 'g':
        pole_x = 7;
        break;
    case 'h':
        pole_x = 8;
        break;
    }

    switch (pole_xy[1]){
    case '1':
        pole_y = 1;
        break;
    case '2':
        pole_y = 2;
        break;
    case '3':
        pole_y = 3;
        break;
    case '4':
        pole_y = 4;
        break;
    case '5':
        pole_y = 5;
        break;
    case '6':
        pole_y = 6;
        break;
    case '7':
        pole_y = 7;
        break;
    case '8':
        pole_y = 8;
        break;
    }

    if (fig == "bishop" && is_diag(fig_x, fig_y, pole_x, pole_y)){
        cout << "YES" << endl;
    } else if (fig == "rook" && is_prime(fig_x, fig_y, pole_x, pole_y)) {
        cout << "YeS" << endl;
    } else if (fig == "queen" && (is_diag(fig_x, fig_y, pole_x, pole_y) || is_prime(fig_x, fig_y, pole_x, pole_y))) {
        cout << "yES" << endl;
    } else {
        cout << "no" << endl;
    }





    return 0;
}
