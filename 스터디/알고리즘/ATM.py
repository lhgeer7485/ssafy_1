N = int(input())

data = list(map(int, input().split()))
result = 0

for x in range(N):
    i = x + 1
    while i < N:
        if data[x] > data[i]:
            swap = data[x]
            data[x] = data[i]
            data[i] = swap
        i += 1

sum = 0

for a in range(N):
    for b in range(0, a+1):
        sum += data[b]
    result += sum
    sum = 0

print(result)