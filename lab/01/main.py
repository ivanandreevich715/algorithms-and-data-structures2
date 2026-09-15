from functools import cmp_to_key
import sys


def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


numbers = []

for line in sys.stdin:
    numbers.append(line.strip())


numbers.sort(key=cmp_to_key(compare))

print(''.join(numbers))