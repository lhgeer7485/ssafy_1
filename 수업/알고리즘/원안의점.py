T = int(input())

for tc in range(1, T+1):
    R = int(input())
    
    cnt = 0

    for i in range(-R, R+1):
        for j in range(-R, R+1):
            if (i ** 2) + (j ** 2) <= R ** 2:
                cnt += 1
    
    print(f'#{tc} {cnt}')