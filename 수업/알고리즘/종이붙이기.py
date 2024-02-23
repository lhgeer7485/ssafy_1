def dp(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3

    if n > 20:
        return dp(n - 10) + (dp(n - 20) * 2)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc} {dp(N)}')
