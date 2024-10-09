# 피보나치
t = int(input())
res = []
# 최대 100까지이므로
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    res.append(dp[n])

for r in res:
    print(r)
