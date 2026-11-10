
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


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


balanced = True

if root is not None:
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if not visited:
            stack.append((node, True))

            if node.right is not None:
                stack.append((node.right, False))

            if node.left is not None:
                stack.append((node.left, False))

        else:
            left_h = node.left.height if node.left else 0
            right_h = node.right.height if node.right else 0

            if abs(left_h - right_h) > 1:
                balanced = False
                break

            node.height = max(left_h, right_h) + 1

print("YES" if balanced else "NO")
