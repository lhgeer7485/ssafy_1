T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = list(map(int, input().split()))

    front = -1
    rear = N - 1

    for x in range(M):
        front += 1
        rear += 1

        data.append(data[front])

    print(f'#{tc} {data[front + 1]}')
