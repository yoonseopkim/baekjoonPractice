n = int(input())
arr = list(map(int, input().split()))
# Write your code here!
dp = [0] * n

dp[0] = arr[0]
max_sum = dp[0]

for i in range(1,n):
    dp[i] = max(arr[i], dp[i-1]+ arr[i])
    max_sum = max(max_sum, dp[i])

print(max_sum)
