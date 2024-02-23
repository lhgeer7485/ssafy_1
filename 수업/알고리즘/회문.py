def fnc(data, N, M):

    index = 0

    is_end = False
    is_search = False

    x = 0

    while not is_end:
        
        li = 0
        ri = li + M - 1
        cnt = 0

        check = M // 2
        if M % 2 == 1:
            check += 1

        result_start = 0

        while True:
            if ri >= N:
                break

            if data[x][ri] != data[x][li]:
                li += 1
                ri = li + M - 1
                cnt = 0

            else:
                result_start = li
                li += 1
                ri -= 1
                cnt += 1

            if cnt == check:
                is_end = True
                index = x
                is_search = True
                
                break

        x += 1

        if x >= len(data):
            is_search = False
            break
    
    return result_start, index, is_search



def fnc_print(result_start, index, data, M):


    
    start = result_start + (M // 2)
    end = result_start - (M // 2)

    if M % 2 == 1:
        end -= 1

    result = ''

    for a in range(start, end, -1):
        result += data[index][a]
    
    print(f'#{tc} {result}')



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [list(input()) for _ in range(N)]

    result_start, index, is_search = fnc(data, N, M)
    
    if is_search:
        fnc_print(result_start, index, data, M)
        

    else:
        zip_data = [[0] * N for _ in range(N)]

        for a in range(N):
            for b in range(N):
                zip_data[a][b] = data[b][a]
   
        result_start, index, is_search = fnc(zip_data, N, M)
        
        fnc_print(result_start, index, zip_data, M)

'''

def find():
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-1-k]:
                    break

    else: # break가 한번도 실행이 안될 경우 수행
        # 회문 찾음
        result = []
        for x in range(j, j+M):
            result.append(data[i][k])
        
        return result

'''
    