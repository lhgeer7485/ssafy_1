T = int(input())

for x in range(T):
    N = int(input())
    data = input()

    count = 0
    max = 0

    for a in range(N):
        
        if a == N-1 and max < count:
            max = count

        if data[a] == '0':

            if max < count:
                max = count

            count = 0
        elif data[a] == '1':
            count += 1

        if a == N-1 and max < count:
            max = count

    print(f'#{x+1} {max}')

    