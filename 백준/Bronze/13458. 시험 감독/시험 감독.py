n = int(input())
# 응시자 수
a = list(map(int, input().split()))
#검독 부감독
b,c = map(int, input().split())
res = n
for s in a:
    if s > b:
        r = s -b
        res += (r + c-1) // c
    
print(res)
        