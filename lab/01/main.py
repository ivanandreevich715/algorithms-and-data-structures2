class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


n = int(input())

points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))


points.sort(key=lambda p: p.x * p.x + p.y * p.y)


for p in points:
    print(p.x, p.y)