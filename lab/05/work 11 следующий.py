
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


def next_value(root, x):
    answer = -1
    current = root

    while current is not None:
        if current.value >= x:
            answer = current.value
            current = current.left
        else:
            current = current.right

    return answer


n = int(sys.stdin.readline())

root = None
last_answer = 0
last_was_query = False

for _ in range(n):
    op, x = sys.stdin.readline().split()
    x = int(x)

    if op == "+":
        if last_was_query:
            x = (x + last_answer) % 1000000000

        root = add(root, x)
        last_was_query = False

    else:
        last_answer = next_value(root, x)
        print(last_answer)
        last_was_query = True
