T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()

    i = 0

    is_pos = True

    while i < N:

        bbang = (data[i] // M) * K

        if bbang < i + 1:
            is_pos = False
            break

        i += 1

    if is_pos:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
