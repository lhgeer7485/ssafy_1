T = int(input())



for test_case in range(T):
    bg = [[0] * 10 for _ in range(10)]
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for x in range(N):
        data[x]
        for i in range(data[x][0], data[x][2]+1):
            for j in range(data[x][1], data[x][3]+1):
                # 레드
                if data[x][4] == 1:
                    if bg[i][j] == 0:
                        bg[i][j] = 'R'
                    if bg[i][j] == 'B':
                        bg[i][j] = 1
                # 블루
                elif data[x][4] == 2:
                    if bg[i][j] == 0:
                        bg[i][j] = 'B'
                    if bg[i][j] == 'R':
                        bg[i][j] = 1

    for i in range(10):
        for j in range(10):
            if bg[i][j] == 1:
                cnt += 1
                
    print(f'#{test_case+1} {cnt}')