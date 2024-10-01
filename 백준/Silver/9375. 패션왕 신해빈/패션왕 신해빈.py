test = int(input())

# 해시는 딕셔너리로 키 - 값
for _ in range(test):
    n = int(input())
    cloth = {}
    for _ in range(n):
        a = input().split()
        cloth_name = a[0]
        cloth_category = a[1]
        # 경우의 수를 체크하는 로직 필요
        if cloth_category in cloth:
            cloth[cloth_category] += 1
        else:
            cloth[cloth_category] = 1
    total = 1
    for c in cloth.values():
        total *= (c + 1)

    res = total - 1
    print(res)

