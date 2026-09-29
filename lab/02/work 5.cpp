#include <iostream>
using namespace std;

bool good(long long a[], int n, int k, long long dist)
{
    int cows = 1;
    long long last = a[0];

    for (int i = 1; i < n; i++)
    {
        if (a[i] - last >= dist)
        {
            cows++;
            last = a[i];
        }
    }

    return cows >= k;
}

int main()
{
    int n, k;
    cin >> n >> k;

    long long a[10000];

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    long long left = 0;
    long long right = a[n - 1] - a[0] + 1;

    while (right - left > 1)
    {
        long long mid = (left + right) / 2;

        if (good(a, n, k, mid))
        {
            left = mid;
        }
        else
        {
            right = mid;
        }
    }

    cout << left;

    return 0;
}