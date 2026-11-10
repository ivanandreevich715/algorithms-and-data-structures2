
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def add(root, x):
    if root is None:
        return Node(x), True

    if x < root.value:
        root.left, added = add(root.left, x)
    elif x > root.value:
        root.right, added = add(root.right, x)
    else:
        return root, False

    return root, added


def search(root, x):
    while root is not None:
        if x == root.value:
            return True
        elif x < root.value:
            root = root.left
        else:
            root = root.right

    return False


def delete(root, x):
    if root is None:
        return None, False

    if x < root.value:
        root.left, deleted = delete(root.left, x)
        return root, deleted

    if x > root.value:
        root.right, deleted = delete(root.right, x)
        return root, deleted

    if root.left is None:
        return root.right, True

    if root.right is None:
        return root.left, True

    predecessor = root.left

    while predecessor.right is not None:
        predecessor = predecessor.right

    root.value, predecessor.value = predecessor.value, root.value
    root.left, _ = delete(root.left, x)

    return root, True


def print_tree(root, level):
    if root is None:
        return

    print_tree(root.left, level + 1)
    print("." * level + str(root.value))
    print_tree(root.right, level + 1)


root = None

for line in sys.stdin:
    command = line.split()

    if command[0] == "ADD":
        x = int(command[1])
        root, added = add(root, x)
        print("DONE" if added else "ALREADY")

    elif command[0] == "DELETE":
        x = int(command[1])
        root, deleted = delete(root, x)
        print("DONE" if deleted else "CANNOT")

    elif command[0] == "SEARCH":
        x = int(command[1])
        print("YES" if search(root, x) else "NO")

    elif command[0] == "PRINTTREE":
        print_tree(root, 0)
