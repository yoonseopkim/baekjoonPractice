a,b = map(int,input().split())

def on(a,b):
    res = 1
    for i in range(a,b + 1):
        if onjun(i):
            res += 1
    return res

def onjun(i):
    if not i % 2 ==0:
     
        if not i % 10 ==5:
        
            if not i % 3 == 0 and i % 9 != 0:
              
                return True

print(on(a,b))