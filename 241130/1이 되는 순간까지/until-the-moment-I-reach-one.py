
def a(n):
    if n==1:
        return 0
    else:
        if n % 2 == 0:
            return 1 + a(n//2) 
        else:
            return 1 + a(n//3) 

n= int(input())
print(a(n))