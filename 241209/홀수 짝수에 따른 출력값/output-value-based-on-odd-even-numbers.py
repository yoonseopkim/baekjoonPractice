def f(n):
    if n % 2 == 0:
        if n == 2:
            return 2
        return n + f(n-2) 
    else:
        if n ==1:
            return 1
        return n + f(n-2)


n = int(input())
print(f(n))