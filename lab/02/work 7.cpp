#include <iostream>
using namespace std;

bool good(long long a[], int n, long long k, long long len)
{
    long long pieces = 0;

    for (int i = 0; i < n; i++)
    {
        pieces += a[i] / len;
    }

    return pieces >= k;
}

int main()
{
    int n;
    long long k;

    cin >> n >> k;

    long long a[10001];
    long long maxLength = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];

        if (a[i] > maxLength)
        {
            maxLength = a[i];
        }
    }

    long long left = 0;
    long long right = maxLength + 1;

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