def fnc(N):
    global next_data
    check = 0

    while True:
        if len(queue) == 1:
            return check_index[check]
        queue[0] //= 2
        if queue[0] == 0:
            queue.pop(0)
            if next_data == M:
                check_index.pop(check)
                N -= 1
                check = check % N
            else:
                queue.append(data[next_data])
                next_data += 1
                check_index[check] = next_data
                check = (check + 1) % N
        else:
            queue.append(queue.pop(0))
            check = (check + 1) % N


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = list(map(int, input().split()))
    check_index = [x for x in range(1, N + 1)]
    next_data = N
    queue = []

    for x in range(N):
        queue.append(data[x])

    print(f'#{tc} {fnc(N)}')
