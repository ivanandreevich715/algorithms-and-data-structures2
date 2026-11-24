
n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

correct = True

for i in range(n):
    if matrix[i][i] != 0:
        correct = False

    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            correct = False

if correct:
    print("YES")
else:
    print("NO")
