data = [int(input()) for _ in range(9)]

for a in range(8):
    index = a
    for b in range(a, 9):
        if data[index] > data[b]:
            index = b
    data[a], data[index] = data[index], data[a]

sum = 0

for x in data:
    sum += x

A, B = 0, 0

for i in range(8):
    for j in range(i+1, 9):
        if sum - data[i] - data[j] == 100:
            A, B = i, j

data.pop(B)
data.pop(A)

for x in data:
    print(x)