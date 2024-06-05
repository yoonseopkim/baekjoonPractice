# m,n = 5,4
m,n = map(int,input().split())
bucket = []
for b in range(m):
    bucket.append(b+1)       # 바구니의 개수만큼 배열 초기화
for index in range(n):
    i,j = map(int,input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]
print(*bucket)
# 21345
# 21435
# 31425
