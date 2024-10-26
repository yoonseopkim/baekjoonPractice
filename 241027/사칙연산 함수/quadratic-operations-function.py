a,o,c = input().split()

def four(a,o,c):
    a = int(a)
    c = int(c)
    res = ''
    if o == '+':
        tmp = a+c
        res = f'{a} + {c} = {tmp}'
    elif o == '-':
        tmp = a-c
        res = f'{a} - {c} = {tmp}'
    elif o == '*':
        tmp = a*c
        res = f'{a} * {c} = {tmp}'
    elif o == '/':
        tmp = a//c
        res = f'{a} / {c} = {tmp}'
    else:
        return False
    return res

print(four(a,o,c))