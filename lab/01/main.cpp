#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int A[1000];

    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    long long count = 0;

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (A[j] > A[j + 1])
            {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;

                count++;
            }
        }
    }

    cout << count;

    return 0;
}