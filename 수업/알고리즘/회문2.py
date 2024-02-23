def fnc(data, N, M):
    for x in range(N):
        start = 0
        end = start + M - 1
        cnt = 0
        is_flag = False

        while end < N:
            
            if data[x][start] == data[x][end]:
                if cnt == (M // 2):
                    is_flag = True
                    return start - cnt, x, is_flag    
                    
                start += 1
                end -= 1
                cnt += 1
            else:
                #start += 1
                start = start - cnt + 1
                end = start + M - 1
                cnt = 0
    
    return 0, 0, is_flag        

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [list(input()) for _ in range(N)]

    i, x, is_flag = fnc(data, N, M)

    result = ''

    if is_flag:

        for a in range(i, i + M):
            result += data[x][a]

    if not is_flag:
        new_data = list(map(list, zip(*data)))
        i, x, is_flag = fnc(new_data, N, M)
        for a in range(i, i + M):
            result += new_data[x][a]

    print(f'#{tc} {result}')