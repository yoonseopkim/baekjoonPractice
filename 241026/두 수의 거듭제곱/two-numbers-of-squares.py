a,b = map(int,input().split())
def c(a,b):
    res = 1
    for i in range(b):
        res *= a
    return res
print(c(a,b))