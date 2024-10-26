m,d = map(int,input().split())

def a(m,d):
    if m in (1,3,5,7,8,10,12):
        if d <= 31:
            return 'Yes'
    elif m in (4,6,9,11):
        if d <= 30:
            return 'Yes'
    elif m == 2:
        if d <= 28:
            return 'Yes'
    else:
        return 'No'

print(a(m,d))