def fnc(data, result):
    for a in range(N):
        t = 0
        for b in reversed(range(N)):
            result[a][t] = data[b][a]
            t += 1
    return result


def fnc2(data):
    for a in range(N):
        st = ''
        for b in range(N):
            st += str(data[a][b])
        data[a] = st
    return data


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    data_90 = [[0] * N for _ in range(N)]
    data_180 = [[0] * N for _ in range(N)]
    data_270 = [[0] * N for _ in range(N)]

    data_90 = fnc(data, data_90)
    data_180 = fnc(data_90, data_180)
    data_270 = fnc(data_180, data_270)

    fnc2(data_90)
    fnc2(data_180)
    fnc2(data_270)

    print(f'#{tc}')
    for x in range(N):
        print(data_90[x], end=' ')
        print(data_180[x], end=' ')
        print(data_270[x])
