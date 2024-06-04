k = int(input())
stack = []  #재민이가 부른 수를 넣는 바구니
res = 0
for i in range(k):
    num = int(input())
    if num == 0:
        res -= stack[-1]  #어짜피 빠질 최상단 스택을 결과에서 뺌
        stack.pop()
    else:
        res += num
        stack.append(num)
print(res)