a,b = map(int,input().split())
def is_prime(a,b):
    res = 0
    for i in range(a,b+1):
        if prime(i):
            res += i 
    return res 

def prime(i):
    for j in range(2, i ):
        if i % j == 0:
            return False
    return True

print(is_prime(a,b))