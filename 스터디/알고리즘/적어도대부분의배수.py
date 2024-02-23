data = list(map(int, input().split()))

min_num = min(data)

while True:

    cnt = 0

    for x in data:
        if min_num % x == 0:
            cnt += 1

    if cnt >= 3:
        print(min_num)
        break

    min_num += 1