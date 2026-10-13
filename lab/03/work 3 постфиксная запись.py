class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()


expression = input().split()

stack = Stack()

for token in expression:
    if token not in "+-*":
        stack.push(int(token))

    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b

        elif token == "-":
            result = a - b

        else:
            result = a * b

        stack.push(result)

print(stack.pop())