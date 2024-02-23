T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    max = 0

    for i in range(N):
        for j in range(N):
            sum = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    if 0 <= a < N and 0 <= b < N:
                        sum += data[a][b]

            if max < sum:
                max = sum

    print(f'#{test_case} {max}')