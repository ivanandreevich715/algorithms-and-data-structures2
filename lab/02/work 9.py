def first_greater_equal(a, x):
    left = -1
    right = len(a)

    while right - left > 1:
        mid = (left + right) // 2

        if a[mid] < x:
            left = mid
        else:
            right = mid

    return right


def first_greater(a, x):
    left = -1
    right = len(a)

    while right - left > 1:
        mid = (left + right) // 2

        if a[mid] <= x:
            left = mid
        else:
            right = mid

    return right


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

for x in b:
    left = first_greater_equal(a, x)
    right = first_greater(a, x)

    print(right - left, end=" ")