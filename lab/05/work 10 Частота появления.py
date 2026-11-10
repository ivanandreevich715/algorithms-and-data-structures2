
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None


root = None

numbers = list(map(int, sys.stdin.read().split()))

for x in numbers:
    if x == 0:
        break

    if root is None:
        root = Node(x)
        continue

    current = root

    while True:
        if x == current.value:
            current.count += 1
            break

        elif x < current.value:
            if current.left is None:
                current.left = Node(x)
                break

            current = current.left

        else:
            if current.right is None:
                current.right = Node(x)
                break

            current = current.right


stack = []
current = root

while current is not None or stack:
    while current is not None:
        stack.append(current)
        current = current.left

    current = stack.pop()

    print(current.value, current.count)

    current = current.right
