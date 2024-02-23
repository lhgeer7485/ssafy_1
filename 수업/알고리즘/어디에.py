T = int(input())

for text_case in range(1, T+1):
    N, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    

    for i in range(N):
        r_cnt = 0 # 행의 연속된 1을 카운트
        c_cnt = 0 # 열의 연속된 1을 카운트
        for j in range(N):
            # 행 부터 체크
            # 값이 1인 경우
            if data[i][j] == 1:
            # 1씩 카운트를 증가시키고
                r_cnt += 1
                # 만약에 1로 끝나는 경우에 K를 만족한다면 결과값을 증가
                if j == N-1 and r_cnt == K:
                    result += 1
                    r_cnt = 0
            # 값이 0인 경우
            elif data[i][j] == 0:
                # 만약에 0 이전까지 체크한 카운트가 K라면 결과값을 증가
                if r_cnt == K:
                    result += 1
                r_cnt = 0 
            
            # 열을 체크
            # 1인 경우
            if data[j][i] == 1:
                c_cnt += 1
                # 1인데 마지막 위치고 지금까지 카운트가 K면 결과값 증가
                if j == N-1 and c_cnt == K:
                    result += 1
                    c_cnt = 0
            # 0인 경우
            elif data[j][i] == 0:
                # 이전까지의 체크값이 K면 결과 증가
                if c_cnt == K:
                    result += 1
                c_cnt = 0

    print(f'#{text_case} {result}')