n, a = map(int,input().split())
nums = list(map(int,input().split()))
stack = []
for num in nums:
    if num < a:
        stack.append(num)
print(*stack)

