# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

	#누적합 최대 
coins = list(map(int,input().split()))
total = 0
sumy = [0] * ( n ) 
dp = [0] * ( n )
dp[0] = coins[0]
total += coins[0]
sumy[0] = coins[0]

for i in range(1, n):
	total += coins[i]
	maxy = max(coins[i] + dp[i-1], coins[i])
	if maxy > dp[i]:
		dp[i] = maxy
	sumy[i] = total
d = max(dp)

s = max(sumy)
# print(d)
# print(s)

	
res = max(d,s)

# 2
# -10 1


# print('디피',dp)
# print('합계',sumy)
# print('둘중에 최대값',maxy)
# print('ekgkqcls 최대값',sumy)
# if res < 0:
# 	res = 0
print(res)

