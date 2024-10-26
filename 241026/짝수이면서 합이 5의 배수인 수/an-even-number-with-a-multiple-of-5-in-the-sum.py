def a(n):
    one = n %10
    ten = n // 10
    tmp = one+ten
    if n % 2 ==0 and tmp % 5 ==0:
        return 'Yes'
    else:
        return 'No'

n = int(input())
print(a(n))