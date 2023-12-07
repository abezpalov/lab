#include <iostream>
#include <fstream>
#include <ctime>
#include <sstream>
#include <string>
#include <cstdio>

#include <limits.h>
#include <unistd.h>

using namespace std;

void numbers1_generate (){

    // Получаем количесвто случайный чисел
    long numbers;
    long numbers_in_line;
    long number;


    cout << "Введите необходимое количество случайных чисел: ";
    cin >> numbers;

    // Рандомизируем рандомизатор
    srand(time(0));

    // Открываем файл, куда будем писать числа
    fstream f_numbers1;
    f_numbers1.open("numbers1.txt", ios::out);

    // Выполняем цикл до тех пор пока у нас остались не сгенерированные числа
    while (numbers > 0) {

        // Генерируем случайное количество чисел в строке от 0 до 10
        // Для получения случайного числа от 0 до 10 берём результат по модулю 11
        numbers_in_line = rand() % 11;

        // Если количество строк в строке больше оставшегося колиества числел, корректируем
        if (numbers_in_line > numbers){
            numbers_in_line = numbers;
        }

        // Генерируем нужное количество чисел в строке
        while (numbers_in_line > 0) {
            number = rand() % 201 - 100;
            f_numbers1 << number;
            numbers--;
            numbers_in_line--;
            if (numbers_in_line > 0) {
                f_numbers1 << ' ';
            }
        }

        // Завершаем строку
        f_numbers1 << endl;

    }
    f_numbers1.close();
}

void file_view(string filename) {

    // Открываем файл, для вывода в консоль
    fstream file;
    file.open(filename, ios::in);

    cout << endl << "Содержимое файла " << filename << ':' << endl;

    // Переменная строки
    string line;

    // Читаем файл построчно
    while (getline(file, line)) {
        cout << line << endl;
    }

    file.close();
}

void numbers2_generate(){

    // Открываем файл
    fstream f_numbers1;
    f_numbers1.open("numbers1.txt", ios::in);

    // Выясняем максимальную длину строки
    int max_len = 0;
    string line;
    while (getline(f_numbers1, line)) {
        if (line.length() > max_len) {
            max_len = line.length();
        }
    }

    // Переоткрываем файл ))))
    f_numbers1.close();
    f_numbers1.open("numbers1.txt", ios::in);
    fstream f_numbers2;
    f_numbers2.open("numbers2.txt", ios::out);

    int spaces;

    while (getline(f_numbers1, line)) {

        // Пишем начальные пробелы
        spaces = max_len - line.length();
        for (int i=0; i<spaces; i++) {
            f_numbers2 << ' ';
        }

        // Дописываем числа
        f_numbers2 << line << endl;

    }

}

void calculate_multiple_of_negative(){

    // Открываем файл
    fstream f_numbers1;
    long number;
    long result = 1;
    f_numbers1.open("numbers1.txt", ios::in);


    // Открываем файл
    fstream f_numbers2;
    f_numbers2.open("numbers2.txt", ios::app);

    // Открываем файл
    fstream f_numbers3;
    f_numbers3.open("numbers3.txt", ios::out);

    // Выбираем отрицательные числа и находим из произведение
    cout << endl << "Отрицательные числа из файла numbers1.txt:" << endl;
    while (f_numbers1 >> number) {
        if (number < 0) {
            f_numbers3 << number << endl;
            cout << number << endl;
            result *= number;
        }
    }

    f_numbers3 << "Result = " << result << endl;
    cout << "Result = " << result << endl;

}


void text2_generate(){

    // Открываем файл
    fstream f_text1;
    f_text1.open("text1.txt", ios::in);

    fstream f_text2;
    f_text2.open("text2.txt", ios::out);

    string line;

    while (getline(f_text1, line)) {

        // Проверяем, со строчной ли буквы начинается строка
        if (islower(line[0])) {
            cout << line << endl;
            f_text2 << line << endl;

        }

    }

}


void text3_generate(){

    // Открываем файл
    fstream f_text2;
    f_text2.open("text2.txt", ios::in);

    // Выясняем максимальную длину строки
    int max_len = 0;
    string line;
    while (getline(f_text2, line)) {
        if (line.length() > max_len) {
            max_len = line.length();
        }
    }

    // Переоткрываем файл ))))
    f_text2.close();
    f_text2.open("text2.txt", ios::in);
    fstream f_text3;
    f_text3.open("text3.txt", ios::out);

    int spaces;

    while (getline(f_text2, line)) {

        // Пишем начальные пробелы
        spaces = (max_len - line.length()) / 2;
        for (int i=0; i<spaces; i++) {
            f_text3 << ' ';
        }

        // Дописываем числа
        f_text3 << line << endl;

    }

}

void total_generate(){

    fstream f_total;
    f_total.open("total.txt", ios::out);

    fstream f_in;
    string line;
    f_in.open("numbers2.txt", ios::in);
    while (getline(f_in, line)) {
        f_total << line << endl;
    }
    f_in.close();

    f_in.open("text3.txt", ios::in);
    while (getline(f_in, line)) {
        f_total << line << endl;
    }
    f_in.close();
    f_total.close();





}

string rename_file(string old_name, string new_name){

    // Просто перепишем содержимое файла в новый файл
    fstream f_in;
    fstream f_out;
    string line;
    f_in.open(old_name, ios::in);
    f_out.open(new_name, ios::out);
    while (getline(f_in, line)) {
        f_out << line << endl;
    }

    return new_name;
}


string getexepath()
{
  char result[ PATH_MAX ];
  ssize_t count = readlink( "/proc/self/exe", result, PATH_MAX );
  return string( result, (count > 0) ? count : 0 );
}

int main() {

    // Включаем поддержку русского языка
    setlocale(LC_ALL, "Russian");

    // Отображаем файл с текстом
    file_view("text1.txt");

    // Генерируем случайные числа
    numbers1_generate();
    file_view("numbers1.txt");

    // Перерисовываем числа c выравниванием по правому краю
    numbers2_generate();
    file_view("numbers2.txt");

    // Подсчитываем произведение отрицтельных чисел в number1.txt
    calculate_multiple_of_negative();

    // Выписываем строки, начинающиеся со строчных букв
    text2_generate();

    // Перерисовываем текст с выравниванием по центру
    text3_generate();
    file_view("text3.txt");

    // Генерируем итоговый файл
    total_generate();

    // Переименовываем итоговый файл
    string old_name;
    string new_name;
    cout << "Введите новое имя для файла " << old_name << ": ";


    cin >>  new_name;


    old_name = getexepath() + old_name;
    new_name = getexepath() + new_name;

    cin << old_name << endl;
    cin << new_name << endl;

    const char * old_name_c = old_name.c_str();
    const char * new_name_c = new_name.c_str();

    rename(old_name_c, new_name_c);


    return 0;
}






