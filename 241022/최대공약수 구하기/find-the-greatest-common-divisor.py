n,m = tuple(map(int,input().split()))

def a(n,m):
    res = 0
    b = 1
    c = min(n,m)
    for i in range (1, c+1):
        if n % i == 0 and m % i ==0:
            res = i
    return res

print(a(n,m))