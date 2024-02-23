T = int(input())

for x in range(T):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    
    station = [0] * (N+1)
    point = 0
    count = 0

    for a in data:
        station[a] = 1

    is_end = False

    while not is_end:

        if point + K >= N:
            break

        for j in reversed(range(point+1, point+K+1)):

            if station[j] == 1:
                point = j
                count += 1
                break

            elif j == point + 1:
                is_end = True
                count = 0
                break

    print(f'#{x+1} {count}')

#####################################################################

    # point = 0
    # count = 0



    # is_end = False

    # while not is_end:

    #     if point + K >= N:
    #         break

    #     for a in data:

            

    #         for j in reversed(range(point+1, point+K+1)):

    #             if j == a:
    #                 point = j
    #                 count += 1
    #                 break

    #             elif j == point + 1:
    #                 is_end = True
    #                 count = 0
    #                 break

    # print(f'#{x+1} {count}')