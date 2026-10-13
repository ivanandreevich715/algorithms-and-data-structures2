from collections import deque
import sys


input = sys.stdin.buffer.readline

n = int(input())

left = deque()
right = deque()

answer = []

for _ in range(n):
    command = input().split()

    if command[0] == b'+':
        right.append(int(command[1]))

    elif command[0] == b'*':
        right.appendleft(int(command[1]))

    else:
        answer.append(str(left.popleft()))

    if len(left) < len(right):
        left.append(right.popleft())


sys.stdout.write("\n".join(answer))