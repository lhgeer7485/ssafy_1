numbers = []

for a in range(9):
    numbers.append(int(input()))

max = -1

for b in range(9):
    if max <= numbers[b]:
        max = numbers[b]
        index = b + 1
print(max)
print(index)