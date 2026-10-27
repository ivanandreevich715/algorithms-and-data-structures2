
#include <iostream>
#include <string>
using namespace std;

class MaxHeap {
private:
    long long heap[200001];
    int heapSize = 0;

public:
    void add(long long x) {
        heapSize++;
        heap[heapSize] = x;

        int i = heapSize;

        while (i > 1 && heap[i] > heap[i / 2]) {
            long long temp = heap[i];
            heap[i] = heap[i / 2];
            heap[i / 2] = temp;

            i = i / 2;
        }
    }

    bool extract(long long &result) {
        if (heapSize == 0) {
            return false;
        }

        result = heap[1];
        heap[1] = heap[heapSize];
        heapSize--;

        int i = 1;

        while (2 * i <= heapSize) {
            int child = 2 * i;

            if (child + 1 <= heapSize &&
                heap[child + 1] > heap[child]) {
                child++;
            }

            if (heap[i] >= heap[child]) {
                break;
            }

            long long temp = heap[i];
            heap[i] = heap[child];
            heap[child] = temp;

            i = child;
        }

        return true;
    }

    void clear() {
        heapSize = 0;
    }
};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    static MaxHeap heap;
    string command;

    while (cin >> command) {
        if (command == "ADD") {
            long long x;
            cin >> x;
            heap.add(x);
        }
        else if (command == "EXTRACT") {
            long long result;

            if (heap.extract(result)) {
                cout << result << '\n';
            }
            else {
                cout << "CANNOT\n";
            }
        }
        else if (command == "CLEAR") {
            heap.clear();
        }
    }

    return 0;
}
