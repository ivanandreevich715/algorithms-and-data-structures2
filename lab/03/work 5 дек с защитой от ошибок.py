from collections import deque


class Deque:
    def __init__(self):
        self.items = deque()

    def push_front(self, value):
        self.items.appendleft(value)

    def push_back(self, value):
        self.items.append(value)

    def pop_front(self):
        return self.items.popleft()

    def pop_back(self):
        return self.items.pop()

    def front(self):
        return self.items[0]

    def back(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return len(self.items) == 0


d = Deque()

while True:
    command = input().split()

    if command[0] == "push_front":
        d.push_front(int(command[1]))
        print("ok")

    elif command[0] == "push_back":
        d.push_back(int(command[1]))
        print("ok")

    elif command[0] == "pop_front":
        if d.is_empty():
            print("error")
        else:
            print(d.pop_front())

    elif command[0] == "pop_back":
        if d.is_empty():
            print("error")
        else:
            print(d.pop_back())

    elif command[0] == "front":
        if d.is_empty():
            print("error")
        else:
            print(d.front())

    elif command[0] == "back":
        if d.is_empty():
            print("error")
        else:
            print(d.back())

    elif command[0] == "size":
        print(d.size())

    elif command[0] == "clear":
        d.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break