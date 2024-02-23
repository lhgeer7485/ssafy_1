def fnc(data, N):
    for a in range(N):
        r_sum = 0
        c_sum = 0
        for b in range(N):
            r_sum += data[a][b]
            c_sum += data[b][a]
        if r_sum != 45 or c_sum != 45 :
            return 0
    
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            sum = 0
            for a in range(i, i+3):
                for b in range(j, j+3):
                    sum += data[a][b]
            if sum != 45:
                return 0


    return 1


T = int(input())
N = 9

for tc in range(1, T + 1):
    data = [list(map(int, input().split())) for _ in range(N)]

    result = fnc(data, N)
    print(f'#{tc} {result}')