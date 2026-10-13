class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


n = int(input())
wagons = list(map(int, input().split()))

stack = Stack()

need = 1

for wagon in wagons:
    stack.push(wagon)

    while not stack.is_empty() and stack.top() == need:
        stack.pop()
        need += 1

if stack.is_empty():
    print("YES")
else:
    print("NO")