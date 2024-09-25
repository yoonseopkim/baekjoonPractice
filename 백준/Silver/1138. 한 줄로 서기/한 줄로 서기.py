n= int(input())
# 사람들 줄
line = list(map(int,input().split()))
# 결과를 담을 , 어떤 키의 사람이 어디에 있는지
res = []
for i in range(n-1,-1,-1):
    res.insert(line[i], i + 1)
print(' '.join(map(str,res)))