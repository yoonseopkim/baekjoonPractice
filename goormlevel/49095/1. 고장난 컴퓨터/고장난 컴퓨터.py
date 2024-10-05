# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, c = map(int,input().split())
# 경과시간
typo = list(map(int,input().split()))

# 코딩 마치고 남아있는 개수 추력
# c 시간을 넘으면 코드가 다 지워지지만 그전에 뭐라도 입력하면 안지워지고 유지됨
dp =[0] * ( n + 1)
dp[0] = typo[0]
# dp[1] = typo[1]
remain_word = 0

for i, val in enumerate(typo):
	if i == 0:
		continue
	#  두 수의 차
	m = val - dp[i-1] 
	dp[i] = val
	if m > c:

		#  모든 코드가 지워저야 함
		remain_word = 0
	#  그게 아니라면 다시 지금 현재 시간부터 계산을 해줘야 한다.
	else:
		remain_word += 1

	
print(remain_word + 1)
		
