T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    for a in range(N-1):
        max_index = a
        min_index = a

        for b in range(a, N):
            if data[max_index] < data[b]:
                max_index = b
            if data[min_index] > data[b]:
                min_index = b

        if a % 2 == 0:
            data[a], data[max_index] = data[max_index], data[a]
        else:
            data[a], data[min_index] = data[min_index], data[a]

    result = data[:10]
    print(f'#{test_case}', *result)