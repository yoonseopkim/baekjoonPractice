n = int(input())
def day(n):
    if n % 4 ==0:
        
        if n % 100 ==0 and n % 400 != 0:
            return 'false' 
        return 'true'
    else:
        return 'false'
print(day(n))