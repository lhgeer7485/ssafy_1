T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    data = [[0] * N for _ in range(N)] 

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    num = 2
    i = 0
    j = 0
    dir = 0
    data[0][0] = 1


    while num <= (N*N):
        ni = i + di[dir]
        nj = j + dj[dir]

    

        if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == 0:
            data[ni][nj] = num
            num += 1
            i = ni
            j = nj
    
        else:
        
            dir = (dir + 1) % 4
    print(f'#{test_case}')
    for x in range(N):
        print(*data[x])

