#include <iostream>
#include <queue>
#include <map>
#include <set>

using namespace std;

class Morojka {

    private:
        long long day; // День, когда его положили в холодильник
        long long rang; // Рейтинг

    public:
        Morojka();
        Morojka(long long day, long long rang);
        ~Morojka();
        bool operator<(const Morojka& m) const;
        long long get_day() const;
        long long get_rang() const;
        void print() const;
};

Morojka::Morojka() {
    this->day = 0;
    this->rang = 0;
};

Morojka::Morojka(long long day, long long rang) {
    this->day = day;
    this->rang = rang;
};

Morojka::~Morojka(){};

bool Morojka::operator<(const Question& q) const{
    // TODO
};

long long Question::get_n() const {
    return this->n;
};

void Question::print() const {
    cout << this->n << " " << this->l << endl;
};

int main() {

    // Считываем количество дней
    long long n;
    cin >> n;

    // Создаём морозильник с мороженным
    long long max_of_morosilka_content = 0;
    priority_queue<long long> morosilka;

    // Множество имём мороженного
    set<string> ice_cream_names;

    // Количество покупок мороженного
    map<string, int> ice_cream_quantities;

    // Да будет время!!
    string name_of_ice;
    long long like_of_ice;
    for (long long i = 0; i<n; i++){
        cin >> name_of_ice >> like_of_ice;

        // Если вкус мороженного лучше, чем в морозилке, покупаем
        if (morosilka.empty() || like_of_ice >= morosilka.top()){

            // Запоминаем ия в упорядоченное множество
            ice_cream_names.insert(name_of_ice);

            // Добавляем в морозилку
            morosilka.push(like_of_ice);

            // Добавляем в подсчёт покупок
            if(ice_cream_quantities.find(name_of_ice) == ice_cream_quantities.end()) {
                ice_cream_quantities[name_of_ice] = 1;
            } else {
                ice_cream_quantities[name_of_ice] += 1;
            }

        // Иначе съедаем из морозилки
        } else {
            morosilka.pop();
        }

        // Обновляем максимум забитости морозилки
        if (morosilka.size() > max_of_morosilka_content){
            max_of_morosilka_content = morosilka.size();
        }
    }

    // Время вышло, считаем и выводим результат

    // Максимум порций
    cout << max_of_morosilka_content << endl;

    // Находим максимум покупок
    long long count_of_max = 0;
    for (auto it = ice_cream_names.begin(); it != ice_cream_names.end(); it++) {
        if (ice_cream_quantities[*it] > count_of_max) {
            count_of_max = ice_cream_quantities[*it];
        }
    }

    // cout << "count_of_max = " << count_of_max << endl;

    // Ещё раз проходим и отбираем лучшие сорта
    set<string> best_of_ice_cream_names;
    for (auto it = ice_cream_names.begin(); it != ice_cream_names.end(); it++) {
        if (ice_cream_quantities[*it] == count_of_max) {
            best_of_ice_cream_names.insert(*it);
        }
    }

    // Выводим что-нибудь
    cout << count_of_max << " " << best_of_ice_cream_names.size() << endl;
    for (auto it = best_of_ice_cream_names.begin(); it != best_of_ice_cream_names.end(); it++) {
        cout << *it << endl;
    }

    return 0;
}
