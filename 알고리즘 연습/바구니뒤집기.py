import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [x for x in range(N+1)]
reverse_range = []
for x in range(M):
    reverse_range.append(list(map(int, input().split())))


for a in range(M):
    i = reverse_range[a][0]
    j = reverse_range[a][1]
    while i < j:
        tmep = numbers[i]
        numbers[i]  = numbers[j]
        numbers[j] = tmep
        i += 1
        j -= 1
del numbers[0]

for x in numbers:
    print(x, end= ' ')