def solve(start, end):
    
    if start == end:
        return start

    
    m = (start + end) // 2
    w1 = solve(start, m)
    w2 = solve(m + 1, end)

    if data[w1] < data[w2]:
        if data[w1] == 1 and data[w2] == 3:
            return w1
        return w2
    elif data[w1] > data[w2]:
        if data[w1] == 3 and data[w2] == 1:
            return w2
        return w1
    else:
        return w1



T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = list(map(int, input().split()))
    
    print(f'#{tc} {solve(0, N - 1) + 1}')
