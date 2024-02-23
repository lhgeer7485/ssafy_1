N, X = map(int, (input().split()))

numbers = list(map(int, input().split()))

for a in range(N):
    if X > numbers[a]:
        print(numbers[a], end=' ')