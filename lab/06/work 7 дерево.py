
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)


if m != n - 1:
    print("NO")

else:
    visited = [False] * n

    stack = [0]
    visited[0] = True

    while stack:
        v = stack.pop()

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)

    if all(visited):
        print("YES")
    else:
        print("NO")
