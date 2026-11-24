
n, s = map(int, input().split())

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


visited = [False] * n


def dfs(v):
    visited[v] = True

    for u in range(n):
        if graph[v][u] == 1 and not visited[u]:
            dfs(u)


dfs(s - 1)

print(sum(visited))
