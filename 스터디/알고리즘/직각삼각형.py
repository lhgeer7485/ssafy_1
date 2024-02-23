while True:
    A, B, C = map(int, input().split())

    if A == 0 and B == 0 and C == 0:
        break

    
    if C < A:
        A, C = C, A
    if C < B:
        B, C = C, B

    if C ** 2 == (A ** 2) + (B ** 2):
        print('right')
    else:
        print('wrong')