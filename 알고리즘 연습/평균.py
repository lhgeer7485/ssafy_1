import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

max = data[0]

for x in range(1,N):
    if data[x] >= max:
        max = data[x]

for x in range(N):
    data[x] = data[x] / max * 100

sum = 0

for x in data:
    sum += x

result = sum/N

print(result)