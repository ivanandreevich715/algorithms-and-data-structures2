import math

C = float(input())

left = 0.0
right = C

for i in range(100):
    mid = (left + right) / 2

    if mid * mid + math.sqrt(mid) < C:
        left = mid
    else:
        right = mid

x = (left + right) / 2

print(f"{x:.6f}")