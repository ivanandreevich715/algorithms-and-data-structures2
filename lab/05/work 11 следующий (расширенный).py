
import sys
import random


class Node:
    __slots__ = ("value", "priority", "left", "right")

    def __init__(self, value):
        self.value = value
        self.priority = random.getrandbits(64)
        self.left = None
        self.right = None


def rotate_right(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root


def rotate_left(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root


def add(root, x):
    if root is None:
        return Node(x)

    if x < root.value:
        root.left = add(root.left, x)

        if root.left.priority > root.priority:
            root = rotate_right(root)

    elif x > root.value:
        root.right = add(root.right, x)

        if root.right.priority > root.priority:
            root = rotate_left(root)

    return root


def next_value(root, x):
    answer = -1

    while root is not None:
        if root.value >= x:
            answer = root.value
            root = root.left
        else:
            root = root.right

    return answer


n = int(sys.stdin.buffer.readline())

root = None
last_answer = 0
last_was_query = False

for _ in range(n):
    op, x = sys.stdin.buffer.readline().split()
    x = int(x)

    if op == b"+":
        if last_was_query:
            x = (x + last_answer) % 1000000000

        root = add(root, x)
        last_was_query = False

    else:
        last_answer = next_value(root, x)
        print(last_answer)
        last_was_query = True
