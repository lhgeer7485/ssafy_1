def find(data, N, M):

    cnt = 0

    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-1-k]:
                    break
                elif k == (M//2) -1:
                    cnt += 1

    return cnt


T = 10

for tc in range(1, T + 1):
    M = int(input())
    N = 8

    data = [list(input()) for _ in range(N)]

    cnt = find(data, N, M)

    zip_data = [[0] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            zip_data[a][b] = data[b][a]

    cnt += find(zip_data, N, M) 

    print(f'#{tc} {cnt}')

