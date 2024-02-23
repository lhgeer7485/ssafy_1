T = int(input())

def serch(P, key):
    start = 1
    end = P
    time = 0

    while start <= end:
        time += 1
        mid = (start + end) // 2
        if mid == key:
            return time
        elif mid < key:
            start = mid
        else:
            end = mid
    return 1001
    
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())

    A_time = serch(P, A)
    B_time = serch(P, B)

    if A_time > B_time:
        print(f'#{test_case} B')
    elif A_time < B_time:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')

    