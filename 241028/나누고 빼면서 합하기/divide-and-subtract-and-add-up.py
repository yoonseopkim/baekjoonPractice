n,m = map(int,input().split())
a = list(map(int,input().split()))

def c():
    global n, m
    res = 0
    while m >= 1:
        if m % 2==0:
            res += a[m-1]
            m //= 2
        else:
            res += a[m-1]
            m -=1 
    return res

print(c())