import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = None
count = 0

numbers = list(map(int, sys.stdin.read().split()))

for x in numbers:
    if x == 0:
        break

    if root is None:
        root = Node(x)
        count += 1
        continue

    current = root

    while True:
        if x == current.value:
            break

        elif x < current.value:
            if current.left is None:
                current.left = Node(x)
                count += 1
                break

            current = current.left

        else:
            if current.right is None:
                current.right = Node(x)
                count += 1
                break

            current = current.right

print(count)