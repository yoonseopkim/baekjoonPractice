a,b = tuple(map(int,input().split()))

#  함수 호출 이후면 RETURN 을 반환해야함
def c(a,b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *=2
    return a,b

print(*c(a,b))