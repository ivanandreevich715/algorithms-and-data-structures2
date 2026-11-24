
n = int(input())

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


color = [0] * n


def dfs(v):
    color[v] = 1

    for u in range(n):
        if graph[v][u] == 1:

            if color[u] == 1:
                return True

            if color[u] == 0:
                if dfs(u):
                    return True

    color[v] = 2
    return False


has_cycle = False

for v in range(n):
    if color[v] == 0:
        if dfs(v):
            has_cycle = True
            break


print(1 if has_cycle else 0)
