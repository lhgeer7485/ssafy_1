N, K = map(int, input().split())
numbers = []

for x in range(N):
    numbers.append(int(input()))

##########


numbers.sort(reverse=True)

count = 0

i = 0

while True:
    # if >> K보다 코인값이 작거나 같으면 K -= 코인, 카운트 ++
    if numbers[i] <= K:
        count += (K // numbers[i])
        K %= numbers[i]
    
    i += 1

    if K <= 0:
        break

print(count)