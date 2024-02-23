import sys
sys.stdin.readline().rsplit()

N = int(input())

data = []
for x in range(N):
    age, st = input().split()
    age = int(age)

    data.append([age, st])

max = -1

for x in range(N):
    if max < int(data[x][0]):
        max = int(data[x][0])

counts = [0] * (max + 1)

for x in range(N):
    counts[data[x][0]] += 1
for i in range(1, len(counts)):
    counts[i] += counts[i-1]
new_data = [0] * N


for i in reversed(range(N)):
    counts[data[i][0]] -= 1
    print(counts[data[i][0]])

    new_data[counts[data[i][0]]] = data[i]



for x in range(N):
    print(*new_data[x])