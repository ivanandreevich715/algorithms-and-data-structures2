
import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
x1, y1, x2, y2 = data[1:5]

sx, sy = x1 - 1, y1 - 1
tx, ty = x2 - 1, y2 - 1

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

dist = [[-1] * n for _ in range(n)]
parent = [[None] * n for _ in range(n)]

queue = deque([(sx, sy)])
dist[sx][sy] = 0

while queue:
    x, y = queue.popleft()

    if (x, y) == (tx, ty):
        break

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

if dist[tx][ty] == -1:
    print(-1)

else:
    print(dist[tx][ty])

    if dist[tx][ty] > 0:
        path = []
        current = (tx, ty)

        while current != (sx, sy):
            path.append((current[0] + 1, current[1] + 1))
            current = parent[current[0]][current[1]]

        path.append((x1, y1))
        path.reverse()

        for x, y in path:
            print(x, y)

