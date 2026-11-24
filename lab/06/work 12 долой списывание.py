
import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
m = data[1]

graph = [[] for _ in range(n)]

index = 2

for i in range(m):
    a = data[index] - 1
    b = data[index + 1] - 1
    index += 2

    graph[a].append(b)
    graph[b].append(a)


color = [0] * n
possible = True

for start in range(n):
    if color[start] == 0:

        queue = deque([start])
        color[start] = 1

        while queue:
            v = queue.popleft()

            for u in graph[v]:
                if color[u] == 0:
                    color[u] = 3 - color[v]
                    queue.append(u)

                elif color[u] == color[v]:
                    possible = False
                    break

            if not possible:
                break

    if not possible:
        break


if possible:
    print("YES")
else:
    print("NO")
