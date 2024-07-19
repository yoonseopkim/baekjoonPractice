def solution(x):
    a = x
    tmp = 0
    while x > 0:
        tmp += x % 10
        x //= 10
    print(tmp)
    if a % tmp == 0:
        return True
    else:
        return False
    