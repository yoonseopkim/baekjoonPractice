n = input()
def p(n):
    a = list(map(str,reversed(n)))
    b = ''.join(a)
    if b == n:
        return 'Yes'
    else:
        return 'No'
print(p(n))