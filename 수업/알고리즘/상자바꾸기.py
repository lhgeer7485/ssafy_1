T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    data = [0] * (N+1)

    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for x in range(L, R+1):
            data[x] = i

    print(f'#{tc}', *data[1:])
