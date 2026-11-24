
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

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

    for i in range(n):
        if color[i] == 1:
            print(i + 1, end=" ")
else:
    print("NO")
