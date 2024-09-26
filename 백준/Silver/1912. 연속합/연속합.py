n = int(input())
#누적합을 더하는 리스트가 필요하다
all_sums = [0] * n

# 수열을 담는 리스트
nums = list(map(int,input().split()))
all_sums[0] = nums[0]
res = all_sums[0]
# dp 면 피보나치, 1번과 2번을 보통 초기화해야함
#1번과 2번 초기화 하는건 피보나치고 여긴 연속합 ! ! !

# 1번만 초기화 하면 된다
for i in range(1, n):
    # 피보나치는 1과 2 전의 수를 현재에 더하는 거지만 지금은 최대를 구해야 한다.
    #핵심 알고리즘 , 현재 해당하는 수와 그 전까지의 누적합을 더한값이 큰지, 아니면 현재 수를 안더한 값이 큰지를 비교하여 최대 누적합을 구한다.
    all_sums[i] = max(nums[i], all_sums[i-1] + nums[i])
    if all_sums[i] > res:
        res = all_sums[i]

# print(all_sums)
print(res)





