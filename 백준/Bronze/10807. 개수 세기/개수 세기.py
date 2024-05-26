n = int(input())
nums = list(map(int, input().split()))
n2 = int(input())
cnt = 0
for num in nums:
    if num == n2:
     cnt += 1
print(cnt)