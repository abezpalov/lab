#include <iostream>
#include <queue>

using namespace std;

class Question {

    private:
        long long n; // Номер вопроса
        long long l; // Длина вопроса

    public:
        Question();
        Question(long long n, long long l);
        ~Question();
        bool operator<(const Question& q) const;
        long long get_n() const;
        void print() const;
};

// Реализация класса Вопрос

Question::Question() {
    this->n = 0;
    this->l = 0;
};

Question::Question(long long n, long long l) {
    this->n = n;
    this->l = l;
};

Question::~Question(){};

bool Question::operator<(const Question& q) const{
    return (this->l < q.l);
};

long long Question::get_n() const {
    return this->n;
};

void Question::print() const {
    cout << this->n << " " << this->l << endl;
};

int main() {

    // Считываем количество вопросов
    long long n;
    cin >> n;

    // Создаём упорядоченную очередь вопросов от сложного к лёгкому
    priority_queue<Question> questions;
    long long l;
    for (long long i = 1; i <= n; i++){
        cin >> l;
        questions.push(Question(i, l));
    }

    // Переносим вопросы в массив
    long long c = questions.size();
    Question *qs = new Question[c];
    for (long long i = 0; i < c; i++) {
        qs[i] = questions.top();
        questions.pop();
    }

    // Обходим массив
    for (long long i = 0; i < c; i++) {
        if (i % 2 == 0){
            cout << qs[i/2].get_n() << endl;
        } else {
            cout << qs[c - i/2 - 1].get_n() << endl;
        }
    }

    return 0;
}
