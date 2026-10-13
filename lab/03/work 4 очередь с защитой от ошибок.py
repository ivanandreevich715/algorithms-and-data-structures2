from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.popleft()

    def front(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()

while True:
    command = input().split()

    if command[0] == "push":
        queue.push(int(command[1]))
        print("ok")

    elif command[0] == "pop":
        if queue.is_empty():
            print("error")
        else:
            print(queue.pop())

    elif command[0] == "front":
        if queue.is_empty():
            print("error")
        else:
            print(queue.front())

    elif command[0] == "size":
        print(queue.size())

    elif command[0] == "clear":
        queue.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break