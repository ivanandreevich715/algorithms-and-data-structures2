def closest(a, x):
    left = -1
    right = len(a)

    # Ищем первый элемент >= x
    while right - left > 1:
        mid = (left + right) // 2

        if a[mid] < x:
            left = mid
        else:
            right = mid

    # Все элементы больше или равны x
    if left == -1:
        return a[right]

    # Все элементы меньше x
    if right == len(a):
        return a[left]

    # Сравниваем двух соседей
    if x - a[left] <= a[right] - x:
        return a[left]
    else:
        return a[right]


n, k = map(int, input().split())

a = list(map(int, input().split()))
requests = list(map(int, input().split()))

for x in requests:
    print(closest(a, x))