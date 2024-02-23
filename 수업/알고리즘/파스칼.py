def pas(N):
    if N >= 2:

        memo_pre = pas(N-1)

        memo[N-1][0] = 1
        memo[N-1][N-1] = 1

        for x in range(1, N-1):
            memo[N-1][x] = memo_pre[x-1] + memo_pre[x]

    return memo[N-1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    memo = [[0] * x for x in range(1, N+1)]
    print(f'#{tc}')

    if N == 1:
        print('1')
        continue

    memo[0] = [1]
    memo[1] = [1, 1]

    pas(N)
    
    for x in memo:
        print(*x)
 