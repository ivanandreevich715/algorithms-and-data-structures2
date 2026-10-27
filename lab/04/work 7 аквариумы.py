
import heapq

n = int(input())

heap = []

for i in range(n):
    a = int(input())

    t = max(1000 - a, 1)

    heapq.heappush(heap, (t, i, a))

last_time = 0
last_pos = 0

while True:
    t, pos, count = heapq.heappop(heap)

    if abs(pos - last_pos) > t - last_time:
        print(t)
        break

    last_time = t
    last_pos = pos

    count += 1
    next_time = t + max(1000 - count, 1)

    heapq.heappush(heap, (next_time, pos, count))
