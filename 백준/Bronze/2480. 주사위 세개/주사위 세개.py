nums = list(map(int, input().split()))
res = 0
cnt = 0
a = []
max_num = max(nums)
if nums[0] == nums[1] == nums[2]:
    res = 10000 + nums[0] * 1000
elif nums[0] == nums[1] != nums[2]: #01
    res = 1000 + nums[0] * 100
elif nums[0] != nums[1] == nums[2]: #12
    res = 1000 + nums[1] * 100
elif nums[0] == nums[2] != nums[1]: #02
    res = 1000 + nums[0] * 100
else:
    res = max_num * 100


print(res)
# 3개가 전부 같을때, 다를때를 구분을 어떻게 하지?
#스택에 담아서 비교? , set 을 써도 될듯
#같은 숫자를 cnt 라 하고 해보기
# 01 같읍 02 같음 12 같음