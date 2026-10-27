
import heapq

n = int(input())

goods = []

for _ in range(n):
    t, l = map(int, input().split())
    goods.append((t, l))

goods.sort()

heap = []

for t, l in goods:
    if heap and heap[0] <= t:
        heapq.heappop(heap)

    heapq.heappush(heap, t + l)

print(len(heap))
