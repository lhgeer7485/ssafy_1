import sys
sys.setrecursionlimit(10 ** 6)

n = int(input()) # 포도주의 개수
data = [0] # 데이터 리스트
dp = [0] * (n+1) # dp[i] : i개의 포도주가 있는경우의 최댓값

"""
n=0이면 포도주가 없는 상태니 결과가 0이다.
그래서 [0]번지 값은 0으로 두고
[1]부터 시작을 한다.
그러므로 n+1개의 공간을 생성한다.
"""

for x in range(n) : # [1]번지부터 데이터를 추가한다
    data.append(int(input()))

dp[1] = data[1] # 포도주가 1개 있는 경우 하나를 선택하면 최댓값

if n >=2 : # 포도주가 2개 있는 경우 2개를 선택하면 최댓값
    dp[2] = data[1] + data[2]

if n >= 3 : # 포도주가 3개 이상인 경우에는 3개 연속으로 선택을 할 수 없으니 여러 경우의 수를 점화식으로 표현
    for i in range(3,n+1): # 3개 이상인 경우를 점화식으로 계산
        dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i], dp[i-1])

print(dp[n])