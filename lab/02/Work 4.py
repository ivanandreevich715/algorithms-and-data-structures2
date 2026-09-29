a, b, c, d = map(int, input().split())


def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


left = -1001.0
right = 1001.0

for i in range(100):
    mid = (left + right) / 2

    if a * f(mid) < 0:
        left = mid
    else:
        right = mid

answer = (left + right) / 2

print(f"{answer:.4f}")