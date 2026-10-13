class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


s = input()

stack = Stack()

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

correct = True

for bracket in s:
    if bracket in "([{":
        stack.push(bracket)

    else:
        if stack.is_empty():
            correct = False
            break

        if stack.pop() != pairs[bracket]:
            correct = False
            break

if not stack.is_empty():
    correct = False

if correct:
    print("yes")
else:
    print("no")