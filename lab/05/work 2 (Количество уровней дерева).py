
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = None
height = 0

numbers = list(map(int, sys.stdin.read().split()))

for x in numbers:
    if x == 0:
        break

    if root is None:
        root = Node(x)
        height = 1
        continue

    current = root
    level = 1

    while True:
        if x == current.value:
            break

        elif x < current.value:
            if current.left is None:
                current.left = Node(x)
                height = max(height, level + 1)
                break

            current = current.left

        else:
            if current.right is None:
                current.right = Node(x)
                height = max(height, level + 1)
                break

            current = current.right

        level += 1

print(height)
