#include <iostream>
#include <string>

using namespace std;

int main() {

    // Считываем количество задач
    long long m_q, l_q;
    cin >> m_q >> l_q;
    long long all = m_q + l_q + 1;

    // Считываем время задач
    long long m_time, l_time;
    cin >> m_time >> l_time;

    // Считываем время теста
    long long time;
    cin >> time;

    long long m_task = 0;
    long long l_task = 0;

    while (true) {

        if (m_q > 0) {
            m_task ++;
            m_q--;
            time -= m_time;
            if (time <= 0){
                cout << "mathan " << m_task;
                break;
            }
        }

        if (l_q > 0) {
            l_task ++;
            l_q--;
            time -= l_time;
            if (time <= 0){
                cout << "linal " << l_task;
                break;
            }
        }

        if (m_q == 0 && l_q == 0) {
            cout << "all " << all;
            break;
        }

    }



    return 0;
}
