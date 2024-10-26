def sam(a,b):
    res = 0
    for i in range(a,b+1):
        if i %3 == 0 or issam(i) == True:
            res += 1
    return res

def issam(i):
    while i > 0:
        if i %10 in (3,6,9) or i // 10 in (3,6,9):

            return True
        i //= 10
a,b = map(int,input().split())
print(sam(a,b))