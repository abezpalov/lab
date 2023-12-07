#include <iostream>
#include <queue>

using namespace std;

class Customer {

    private:
        long long n;
        long long time_for_start;
        long long time_for_end;

    public:
        Customer(long long _n, long long _time_for_start, long long _time_for_end);
        ~Customer();
        bool operator<(const Customer& customer) const;
        long long get_time_for_start() const;
        long long get_time_for_end() const;
        void print() const;
};

class Kassa {

    private:
        long long n;
        long long time_of_work;
        long long count_of_customers;
        long long time_of_end_operations;

    public:
        Kassa();
        Kassa(long long _n);
        ~Kassa();
        bool operator<(const Kassa& kassa) const;
        void operator+(const Customer& customer);
        long long get_n() const;
        long long get_time_of_work() const;
        long long get_count_of_customers() const;
        long long get_time_of_end_operations() const;
        void set_time_of_end_operations(long long time_of_end_operations_);
        void print() const;
};


// Реализация класса Покупатель

Customer::Customer(long long _n, long long _time_for_start, long long _time_for_end) {
    n = _n;
    time_for_start = _time_for_start;
    time_for_end = _time_for_end;
};

Customer::~Customer(){};

bool Customer::operator<(const Customer& customer) const{
    return ((this->time_for_start > customer.time_for_start) || ((this->time_for_start == customer.time_for_start) && (this->n > customer.n)));
};

long long Customer::get_time_for_start() const {
    return this->time_for_start;
};

long long Customer::get_time_for_end() const {
    return this->time_for_end;
};

void Customer::print() const {
    cout << "Customer " << n << " " <<  time_for_start << " " << time_for_end << endl;
};

// Реализация класса Касса

Kassa::Kassa() {
    n = 0;
    time_of_work = 0;
    count_of_customers = 0;
    time_of_end_operations = 0;
};

Kassa::Kassa(long long _n) {
    n = _n;
    time_of_work = 0;
    count_of_customers = 0;
    time_of_end_operations = 0;
};

Kassa::~Kassa(){};

bool Kassa::operator<(const Kassa& kassa) const{
    return (this->time_of_end_operations > kassa.time_of_end_operations) || ((this->time_of_end_operations == kassa.time_of_end_operations) && (this->n > kassa.n));
};

void Kassa::operator+(const Customer& customer){
    this->time_of_work = this->time_of_work + customer.get_time_for_end();
    this->count_of_customers++;
};

long long Kassa::get_n() const {
    return this->n;
};

long long Kassa::get_time_of_work() const {
    return this->time_of_work;
};

long long Kassa::get_count_of_customers() const {
    return this->count_of_customers;
};

long long Kassa::get_time_of_end_operations() const {
    return this->time_of_end_operations;
};

void Kassa::set_time_of_end_operations(long long time_of_end_operations_) {
    this->time_of_end_operations = time_of_end_operations_;
};

void Kassa::print() const {
    cout << "Kassa " << n << " " <<  time_of_work << " " << count_of_customers << " " << time_of_end_operations << endl;
};


int main() {

    long long q_of_kasses;
    long long q_of_customers;

    cin >> q_of_kasses >> q_of_customers;

    // Создаём очереди с кассами
    priority_queue<Kassa> free_kasses;
    priority_queue<Kassa> worked_kasses;
    for (long long i = 0; i < q_of_kasses; i++){
        free_kasses.push(Kassa(i));
    }

    // Создаём очередь покупателей
    priority_queue<Customer> customers;
    long long time_for_start;
    long long time_for_end;
    for (long long i = 0; i < q_of_customers; i++){
        cin >> time_for_start >> time_for_end;
        customers.push(Customer(i, time_for_start, time_for_end));
    }

    // Да будет время!!
    long long t = 0;

    // Время идём до тех пор, пока есть необслуженные клиенты или работающе кассы
    while(!customers.empty() || !worked_kasses.empty()) {

        // Освобождаем отработавшие кассы
        while(!worked_kasses.empty() && worked_kasses.top().get_time_of_end_operations() <= t) {

            // cout << "Point 3: " << t << " " << customers.size() << " " << free_kasses.size() << " " << worked_kasses.size() << endl;

            // Инициализируем временные переменные
            Kassa kassa = worked_kasses.top(); // TODO

            // Актуализируем информацию в кассе
            kassa.set_time_of_end_operations(0);

            // Переносим
            free_kasses.push(kassa);
            worked_kasses.pop();
        }

        // Направляем посетителей по свободным кассам
        while(!customers.empty() && (customers.top().get_time_for_start() <= t) && !free_kasses.empty()){

            // Инициализируем временные переменные
            Customer customer = customers.top(); // TODO
            Kassa kassa = free_kasses.top(); // TODO

            // Актуализируем информацию в кассе
            kassa + customer;
            kassa.set_time_of_end_operations(t + customer.get_time_for_end());

            // Переносим
            customers.pop();
            worked_kasses.push(kassa);
            free_kasses.pop();
        }
        t++;
    }

    t--;

    // Выводим очередь касс
    while(!free_kasses.empty()){
        Kassa kassa = free_kasses.top();
        cout << kassa.get_count_of_customers() << " " << t - kassa.get_time_of_work() << endl;
        free_kasses.pop();
    }

    return 0;
}
