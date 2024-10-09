
# 원판개수, 1번,2번,3번 장대
def fibo(n, start, middle, end):
    # 원판이 한개면 바로 3번 장대로 옮기기
    if n ==1 :
        print(start, end)
        return
    # 그게 아니면 2번 장대에 전부 떄려박기
    # 그다음에 가장 큰 원판을 3번 장대에 넣기
    else:
        fibo(n-1,start, end, middle)
        print(start, end)
        # 잔챙이를 2번에 놓고 가장 무거운 원판을 1번에서 3번으로 옮기는게 먼저다 !
        fibo(n-1, middle, start, end)
# 2 1 2 3
# 1 1 3 2
# 1 2 출력



n = int(input())
# gkshdl 하노이 공식
print(2**n -1)
fibo(n,1,2,3)
