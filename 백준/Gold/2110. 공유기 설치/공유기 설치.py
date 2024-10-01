n, c=  map(int,input().split())
home = []
for _ in range(n):
    # 집의 좌표
    h = int(input())
    home.append(h)
# 이진 탐색을 위해 필수적인 조건
home.sort()
# 이분탐색으로 점진적으로 줄이기

l = 1
r  = home[-1] - home[0]
# 공유기 사이의 최대 거리
res = 0

#  넘어가는 순간 루프를 종료시켜야 한다.
while l <= r :
    mid = (l + r )// 2
    # 종료 조건을 표시해야 한다.
    #마지막으로 공유기 설치한 집 위치
    curr = home[0]
    cnt = 1

    for i in range(1,n):
        if home[i] - curr >= mid:
            cnt += 1
            curr = home[i]

    # 공유기가 더 멀어져야 할경우
    if cnt >= c:
        res = mid
        l = mid + 1
    # 공유기가 더 가까워져야 할경우
    else:
        r = mid -1

print(res)