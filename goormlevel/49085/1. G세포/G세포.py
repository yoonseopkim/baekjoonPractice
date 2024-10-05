# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
n = int(input())
tmp = [] 
ans = []
ans_count = 0
while n >0:
	# print(n)
	tmp.append(n % 2)
	n //= 2
	
# print('tmp', tmp)
tmp_index = 0
for i,val in enumerate(tmp):
	tmp_index = i
	if val == 0:
		continue
	else:
		ans_count += 1
		ans.append(i)
		# if i == 0:
		# 	ans.append(1)
		# elif i == 1:
		# 	ans.append(2)
		# # 진짜 제곱해주기
		# else:	
		# 	ans.append(i)
			
# print('ans', ans)
print(ans_count)
print(' '.join(map(str,ans)))
		



# 1 + 2 = 3 // 1 + 2 + 8 // 4 + 8 + 16
# 2의 제곱 -> 2진수로 바꾸면 끝