N = int(input())

numbers = list(map(int, input().split()))

min = 1000001
max = -1000001

for a in range(N):

    if max < numbers[a]:
        max = numbers[a]

    if min > numbers[a]:
        min = numbers[a]

print(f'{min} {max}')