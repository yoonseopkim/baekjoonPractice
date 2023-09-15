s = input().strip()

cur = s[0]
cnt = 0

for i in s[1:]:
    if i != cur:
        cnt += 1
        cur = i
print(cnt //2 + cnt % 2)