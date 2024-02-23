import sys
sys.stdin = open('input.txt', 'r')
T = 10
M = 100
for test_case in range(T):
    N = int(input())
    

    data = [list(map(int, input().split())) for _ in range(M)]

    #좌상 우상 좌하 우하
    
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]

    max = 0

    for i in range(M):
        r_sum = 0
        c_sum = 0
        for j in range(M):
            x_sum = 0          
            r_sum += data[i][j]
            c_sum += data[j][i]
            
            for a in range(4):

                ni = i + di[a]
                nj = j + di[a]

                if 0 <= ni < M and 0 <= nj < M:
                    #print(data[ni][nj])
                    x_sum += data[ni][nj]
           
            if max < x_sum:
                max = x_sum
        
            if max < r_sum:
                max = r_sum
            if max < c_sum:
                max = c_sum
            #print(f'max {max}')
    print(f'#{test_case+1} {max}')

'''
1
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''