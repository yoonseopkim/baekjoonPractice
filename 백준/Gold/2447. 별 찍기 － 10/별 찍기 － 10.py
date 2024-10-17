import sys
sys.setrecursionlimit(10000)
def draw_square(n):
    if n == 1:
        # 이게 한덩어리
        return ['*']

    smaller_square = draw_square(n // 3)

    top = [row * 3 for row in smaller_square]
    middle = [row + ' ' * len(smaller_square) + row for row in smaller_square]

    return top + middle + top

n = int(input())
res = draw_square(n)
for r in res:
    print(r)

