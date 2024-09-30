# 첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L
n, l = map(int, input().split())
#v 항승이가 필요한 테이프의 개수
res = 0
#테이프의 끝 길이
tape_len = 0

#둘째 줄에는 물이 새는 곳의 위치가 주어진다.
water = list(map(int, input().split()))

# 누수 지점을 오름차순 정렬해야함 원인?
water.sort()


for w in water:
    # 누수가 테이프 길이보다 길경우
    if w > tape_len:
        res += 1
        # 좌,우 0.5 씩 커버해야하므로 1을 ㄷ더 뺸다
        tape_len = w + l - 1

print(res)



