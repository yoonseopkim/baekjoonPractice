T = int(input())
a = 300
b = 60
c = 10
a_count = 0
b_count = 0
c_count = 0

if T >= a:
    a_count = T // a
    T %= a
if T>=b:
    b_count = T // b
    T %= b
if T>=c:
    c_count = T // c
    T %= c
if T==0:

    print(a_count,b_count,c_count)
else:
    print(-1)
