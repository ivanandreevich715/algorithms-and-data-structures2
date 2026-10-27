
import sys


def sift_down(a, i, size):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < size and a[left] > a[largest]:
            largest = left

        if right < size and a[right] > a[largest]:
            largest = right

        if largest == i:
            break

        a[i], a[largest] = a[largest], a[i]
        i = largest


def heap_sort(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(a, i, n)

    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)


data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:n + 1]

heap_sort(a)

print(*a)

