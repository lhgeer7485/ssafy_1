# 부분집합의 합
                
def print_subset(bit, arr, n):
    total = 0
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
    print(bit, total)

arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

for a in range(2):
    bit[0] = a
    for b in range(2):
        bit[1] = b
        for c in range(2):
            bit[2] = c
            for d in range(2):
                bit[3] = d
                print_subset(bit, arr, 4)