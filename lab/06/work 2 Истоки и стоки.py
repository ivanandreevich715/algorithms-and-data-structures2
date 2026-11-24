
n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


sources = []
sinks = []

for i in range(n):

    #Проверяем, является ли вершина истоком
    if all(matrix[j][i] == 0 for j in range(n)):
        sources.append(i + 1)

    #Проверяем, является ли вершина стоком
    if all(matrix[i][j] == 0 for j in range(n)):
        sinks.append(i + 1)


print(len(sources))
for v in sources:
    print(v)

print(len(sinks))
for v in sinks:
    print(v)
