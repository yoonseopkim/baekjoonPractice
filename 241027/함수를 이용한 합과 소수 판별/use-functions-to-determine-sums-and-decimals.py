a,b = map(int,input().split())
def is_print(a,b):
    res = 0
    for i in range(a,b+1):
        if is_prime(i) and is_even(i):
            res += 1
    return res

def is_prime(i):
    for j in range(2,i):
        if i % j ==0:
            return False
    return True

def is_even(i):
    if (i % 10 + i //10) % 2 ==0:
        return True
    return False
    


print(is_print(a,b))