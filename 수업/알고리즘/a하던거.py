def fnc(i):
    global max_v
    if i == K:
        st = ''.join(numbers)
       # print(st)
        if max_v < int(st):
            max_v = int(st)
        return

    for a in range(N):
        for b in range(a + 1, N):
            numbers[a], numbers[b] = numbers[b], numbers[a]
            st = ''.join(numbers)
            # print(st)
            if st not in check:
                #print(check, st, a, b)
                check.append(st)
                fnc(i + 1)
            numbers[a], numbers[b] = numbers[b], numbers[a]
    #print(check)

T = int(input())
for tc in range(1, T + 1):
    numbers, K = map(int, input().split())
    numbers = list(str(numbers))

    check = []

    max_v = 0
    N = len(numbers)
    fnc(0)
    print(f'#{tc} {max_v}')
