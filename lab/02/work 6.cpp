#include <iostream>
#include <algorithm>
using namespace std;

bool good(long long time, long long n, long long x, long long y)
{
    return time / x + time / y >= n;
}

int main()
{
    long long n, x, y;
    cin >> n >> x >> y;

    if (x > y)
    {
        swap(x, y);
    }

    // Первую копию делаем на более быстром ксероксе
    long long firstCopy = x;

    // Осталось сделать n - 1 копий
    n--;

    long long left = 0;
    long long right = n * x;

    while (right - left > 1)
    {
        long long mid = (left + right) / 2;

        if (good(mid, n, x, y))
        {
            right = mid;
        }
        else
        {
            left = mid;
        }
    }

    cout << firstCopy + right;

    return 0;
}