T = int(input())
N = 5
for tc in range(1, T + 1):
    data = [input() for _ in range(N)]

    M = 0

    for x in data:
        if M < len(x):
            M = len(x)

    st = ''

    for i in range(M):
        for j in range(M):
            try:
                st += data[j][i]
            except:
                pass

    print(f'#{tc} {st}')