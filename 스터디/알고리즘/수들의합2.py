N, M = map(int, input().split())

numbers = list(map(int, input().split()))
count = 0
start, end = 0, 1

while start <= end and end <= N:
    result = sum(numbers[start:end])
    if result == M:
        count += 1
        start += 1
        end = start + 1

    elif result < M:
        end += 1

    else:
        start += 1
        end = start + 1

print(count)