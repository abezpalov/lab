#include <iostream>

using namespace std;

int main() {

    // Считываем данные
    int n, m;
    cin >> n >> m;

    // Задаём начальное состояние полосок и долек в отломанной полоске
    int n_dolek = 0;
    int n_polosok = n;

    int result = 0;

    while(true){

        // Если долько кончились, и можно сразу доесть
        if (n_dolek == 0 && n_polosok == 1 && m <= 3) {
            n_polosok--;
            break;
        }

        // Если дольки не закончились, но их можно доесть за раз
        if (n_dolek <= 3 && n_polosok == 0) {
            n_dolek = 0;
            break;
        }




        // Если долько кончились, но можно отломить
        if (n_dolek == 0 && n_polosok > 1) {
            result++;
            n_dolek = m;
            n_polosok--;
            continue;
            // Поедим позже
        }



        // Если дольки кончились, и осталась последняя полоска
        if (n_dolek == 0 && n_polosok == 1 && m > 3) {
            n_dolek = m;
            n_polosok--;
            continue;
            // Поедим позже
        }

        // Если одна долька, но есть ещё полоски
        if (n_dolek == 1 and n_polosok == 1){
            n_dolek = m+1;
            n_polosok--;
            continue;
            // Поедим позже
        }

        // Если одна долька, но есть ещё полоски
        if (n_dolek == 1 and n_polosok > 1){
            result++;
            n_dolek = m+1;
            n_polosok--;
            continue;
            // Поедим позже
        }

        // Если две дольки
        if (n_dolek == 2) {
            n_dolek = 0;
            continue;
        }

        // Если больше двух долек
        if (n_dolek > 2){
            n_dolek -= 2;
            result++;
            continue;
        }

    }

    cout << result << endl;

    return 0;
}
