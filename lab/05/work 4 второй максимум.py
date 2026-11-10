import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def add(root, x):
    if root is None:
        return Node(x)

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

    return root


def second_max(root):
    parent = None
    current = root

    while current.right is not None:
        parent = current
        current = current.right

    if current.left is not None:
        current = current.left

        while current.right is not None:
            current = current.right

        return current.value

    return parent.value


root = None

numbers = list(map(int, sys.stdin.read().split()))

for x in numbers:
    if x == 0:
        break

    root = add(root, x)

print(second_max(root))
