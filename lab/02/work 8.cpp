#include <iostream>
#include <algorithm>
using namespace std;

bool good(long long side, long long w, long long h, long long n)
{
    long long byWidth = side / w;
    long long byHeight = side / h;

    return (__int128)byWidth * byHeight >= n;
}

int main()
{
    long long w, h, n;
    cin >> w >> h >> n;

    long long left = 0;
    long long right = max(w, h) * n;

    while (right - left > 1)
    {
        long long mid = (left + right) / 2;

        if (good(mid, w, h, n))
        {
            right = mid;
        }
        else
        {
            left = mid;
        }
    }

    cout << right;

    return 0;
}