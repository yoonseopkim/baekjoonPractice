T = int(input())
a = 300
b = 60
c = 10
a_counter = 0
b_counter = 0
c_counter = 0
change = 0
change1 = 0

if T >=a:
    a_counter = T// a
    T = T - a_counter * a

if T >= b:
    b_counter = T // b
    T = T - b_counter * b
if T >= c:
    c_counter = T // c
    T = T - c_counter * c
if T==0:
    print(a_counter,b_counter,c_counter)
else:
    print(-1)










