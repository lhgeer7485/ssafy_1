import sys
input = sys.stdin.readline
num = list(map( int, input().strip()))

for a in range(len(num)):
    max = num[a]
    i = a
    for b in range(a, len(num)):
        if num[b] > max:
            i = b
            max = num[b]
        
    tmp = num[a]
    num[a] = num[i]
    num[i] = tmp
            

for x in num:
    print(x, end='')