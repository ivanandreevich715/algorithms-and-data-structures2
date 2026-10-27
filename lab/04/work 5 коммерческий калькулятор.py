import heapq

n = int(input())
numbers = list(map(int, input().split()))

heapq.heapify(numbers)

total = 0

while len(numbers) > 1:
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)

    result = a + b
    total += result

    heapq.heappush(numbers, result)



print(f"{total * 0.05:.2f}")