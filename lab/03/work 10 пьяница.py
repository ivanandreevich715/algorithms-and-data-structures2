from collections import deque


first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

moves = 0

while first and second and moves < 1000000:
    a = first.popleft()
    b = second.popleft()

    if (a == 0 and b == 9) or (a > b and not (a == 9 and b == 0)):
        first.append(a)
        first.append(b)
    else:
        second.append(a)
        second.append(b)

    moves += 1


if moves == 1000000 and first and second:
    print("botva")
elif first:
    print("first", moves)
else:
    print("second", moves)