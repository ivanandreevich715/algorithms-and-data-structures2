class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def back(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()

while True:
    command = input().split()

    if command[0] == "push":
        stack.push(int(command[1]))
        print("ok")

    elif command[0] == "pop":
        if stack.is_empty():
            print("error")
        else:
            print(stack.pop())

    elif command[0] == "back":
        if stack.is_empty():
            print("error")
        else:
            print(stack.back())

    elif command[0] == "size":
        print(stack.size())

    elif command[0] == "clear":
        stack.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break