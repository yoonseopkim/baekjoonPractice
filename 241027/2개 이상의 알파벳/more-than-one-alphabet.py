from collections import Counter 
a = input()
def b(a):


    a1   = Counter(a)
    if len(a1) == 1:
        return 'No'
    else:
        return 'Yes'
print(b(a))