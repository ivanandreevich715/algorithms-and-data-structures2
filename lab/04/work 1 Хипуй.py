import sys


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] >= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def extract(self):
        maximum = self.heap[0]
        last = self.heap.pop()

        if not self.heap:
            return maximum

        self.heap[0] = last
        i = 0
        n = len(self.heap)

        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2

            largest = left

            if right < n and self.heap[right] > self.heap[left]:
                largest = right

            if self.heap[i] >= self.heap[largest]:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

        return maximum


n = int(sys.stdin.readline())
heap = MaxHeap()

for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 0:
        heap.insert(command[1])
    else:
        print(heap.extract())
