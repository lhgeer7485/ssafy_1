import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    i = 0
    max_i = 0
    result = 0

    while i < N - 1:

        cost = 0
        cnt = 0

        # 최대값을 구해
        max_i = i
        for x in range(i, N):
            if data[max_i] <= data[x]:
                max_i = x

        if i == max_i:
            i += 1
            
            continue

        for a in range(i, max_i):
            cost += data[a]
            cnt += 1
        result += (data[max_i] * cnt) - cost
        i = max_i

    print(f'#{tc} {result}')
