import random

def quick_sort(a, left, right):
    if left >= right:
        return

    pivot = a[random.randint(left, right)]

    i = left
    j = right

    while i <= j:
        while a[i] < pivot:
            i += 1

        while a[j] > pivot:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if left < j:
        quick_sort(a, left, j)

    if i < right:
        quick_sort(a, i, right)


n = int(input())
a = list(map(int, input().split()))

quick_sort(a, 0, n - 1)

print(*a)