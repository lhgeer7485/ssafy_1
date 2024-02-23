import sys
input = sys.stdin.readline

K = int(input())
data = []
for x in range(K):
    num = int(input())
    if num != 0:
        data.append(num)
    else:
        data.pop()

sum = 0

for x in range(len(data)):
    sum += data[x]

print(sum)    

