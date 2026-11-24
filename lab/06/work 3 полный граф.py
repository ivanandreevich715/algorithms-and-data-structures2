
n, m = map(int, input().split())

edges = set()

for i in range(m):
    a, b = map(int, input().split())

    if a != b:
        edges.add((min(a, b), max(a, b)))


complete = True

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i, j) not in edges:
            complete = False
            break

    if not complete:
        break


print("YES" if complete else "NO")