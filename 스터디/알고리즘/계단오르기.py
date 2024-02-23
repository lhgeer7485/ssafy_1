import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

data = [0]
dp = [0] * (N + 1)

for x in range(N):
    data.append(int(input()))

dp[1] = data[1]

if N >= 2:
    dp[2] = data[1] + data[2]

if N >= 3:
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i])

print(dp[N])