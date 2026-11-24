
from collections import deque

n = int(input())

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

s, t = map(int, input().split())

s -= 1
t -= 1

dist = [-1] * n
parent = [-1] * n

dist[s] = 0

queue = deque([s])

while queue:
    v = queue.popleft()

    for u in range(n):
        if graph[v][u] == 1 and dist[u] == -1:
            dist[u] = dist[v] + 1
            parent[u] = v
            queue.append(u)


if dist[t] == -1:
    print(-1)

else:
    print(dist[t])

    if dist[t] > 0:
        path = []
        current = t

        while current != s:
            path.append(current + 1)
            current = parent[current]

        path.append(s + 1)
        path.reverse()

        print(*path)
