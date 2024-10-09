n = int(input())
dp = [0] * 100
#  결과값,세준이가 얻을 수 있는 최대 기쁨을 출
max_bliss = 0
hp_minus = list(map(int,input().split()))
bliss = list(map(int,input().split()))

for i in range(n):
    for j in range(99, hp_minus[i]-1, -1):
        if dp[j-hp_minus[i]] + bliss[i] > dp[j]:
            dp[j] = dp[j - hp_minus[i]] + bliss[i]

print(max(dp))
