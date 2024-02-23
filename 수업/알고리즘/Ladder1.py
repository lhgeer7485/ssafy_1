

T = 100

for test_case in range(1, 11):
    t = int(input())

    data = [list(map(int, input().split())) for _ in range(T)]

    for i in range(T):
        for j in range(T):
            if data[i][j] == 2:
                start_i = i
                start_j = j

    # 좌 우 상
    di = [0, 0, -1]
    dj = [-1, 1, 0]

    point_i = start_i
    point_j = start_j

    is_gone = 'up'

    while point_i:    


        # print(point_i, point_j)   

        for x in range(3):
            ni = point_i + di[x]
            nj = point_j + dj[x]

            if 0 <= ni < T and 0 <= nj < T:
                if data[ni][nj] == 1:
                    # 왼쪽
                    if x == 0:
                        if is_gone == 'right':
                            continue
                        point_i = ni
                        point_j = nj
                        is_gone = 'left'
                        break
                    # 오른쪽
                    elif x == 1:
                        if is_gone == 'left':
                            continue
                        point_i = ni
                        point_j = nj
                        is_gone = 'right'
                        break
                # 2까지 왔다는것은 좌우 모두 0이라는 뜻
                if x == 2:
                    point_i = ni
                    point_j = nj
                    is_gone = 'up'

                # 좌우 확인 끝나고 위로 한칸
                
                
        
    print(f'#{test_case} {point_j}')