
import sys

n, m = map(int, sys.stdin.buffer.readline().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.buffer.readline().split())

    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)


visited = [False] * n
components = []

for start in range(n):
    if not visited[start]:

        stack = [start]
        visited[start] = True

        component = []

        while stack:
            v = stack.pop()
            component.append(v)

            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        components.append(component)


print(len(components))

for component in components:
    print(len(component))
    print(*(v + 1 for v in component))
