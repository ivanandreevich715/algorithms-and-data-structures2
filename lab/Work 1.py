def binary_search(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return True

        elif a[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return False


n, k = map(int, input().split())

a = list(map(int, input().split()))
requests = list(map(int, input().split()))

for x in requests:
    if binary_search(a, x):
        print("YES")
    else:
        print("NO")