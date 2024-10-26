a,b = map(int,input().split())

def on(a,b):
    res = 0
    for i in range(a,b + 1):
        if onjun(i):
            res += 1
    return res

def onjun(i):
    if i % 2 == 0:
        return False
    elif i % 10 ==5:
        return False
    elif i % 3 == 0 and i % 9 != 0:
        return False
    else:
        return True


print(on(a,b))