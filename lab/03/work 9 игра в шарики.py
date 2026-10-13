import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
balls = data[1:n + 1]

groups = []

for ball in balls:
    if groups and groups[-1][0] == ball:
        groups[-1][1] += 1
    else:
        groups.append([ball, 1])


stack = []
destroyed = 0

for color, count in groups:

    if stack and stack[-1][0] == color:
        stack[-1][1] += count
    else:
        stack.append([color, count])

    if stack[-1][1] >= 3:
        destroyed += stack[-1][1]
        stack.pop()


print(destroyed)