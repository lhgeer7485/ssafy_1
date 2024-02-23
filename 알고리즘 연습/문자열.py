import sys
input = sys.stdin.readline

T = int(input())
sts = []

for x in range(T):
    sts.append(input().rstrip())

for x in range(T):
    print(f'{sts[x][0]}{sts[x][len(sts[x])-1]}')