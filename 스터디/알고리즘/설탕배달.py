N = int(input())
result = 0

while True :
    if N % 5 == 0 :
        result += N // 5
        break
    elif N < 3 :
        result = -1
        break

    N -= 3
    result += 1

print(result)