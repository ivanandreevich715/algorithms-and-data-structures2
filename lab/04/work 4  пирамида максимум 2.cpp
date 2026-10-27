
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    priority_queue<long long> heap;
    string command;

    while (cin >> command) {
        if (command == "ADD") {
            long long x;
            cin >> x;
            heap.push(x);
        }
        else if (command == "EXTRACT") {
            if (heap.empty()) {
                cout << "CANNOT\n";
            }
            else {
                cout << heap.top() << '\n';
                heap.pop();
            }
        }
        else if (command == "CLEAR") {
            heap = priority_queue<long long>();
        }
    }

    return 0;
}
