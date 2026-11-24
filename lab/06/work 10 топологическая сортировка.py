
import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
m = data[1]

edges = []
index = 2

for i in range(m):
    u = data[index] - 1
    v = data[index + 1] - 1
    edges.append((u, v))
    index += 2

order = data[index:index + n]

pos = [0] * n

for i in range(n):
    pos[order[i] - 1] = i

correct = True

for u, v in edges:
    if pos[u] >= pos[v]:
        correct = False
        break

if correct:
    print("YES")
else:
    print("NO")
