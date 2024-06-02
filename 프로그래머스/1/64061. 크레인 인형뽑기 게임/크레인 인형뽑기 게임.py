def solution(board,moves):
    stack = []  #인형담는 바구니
    res = 0  # 터진 인형
    for i,val1 in enumerate(moves):  #move가 일단 1 , 그다음 5로 예시, 열이 고정되야함.  왜 i가 5에서 짤리지? len 은 7인데
        for j,val2 in enumerate(board):  #보드에 moves -1 이 인덱스임.
            print(board[j][val1-1],end="")  # board가 5까지니까 !! val 1을 히야하는거네 !
            if board[j][val1-1]  == 0:
                continue  #0이면 인형이 없는 거니까 그냥 패스하기
            elif stack and stack[-1] == board[j][val1-1]:  #val 에서 1뺴준이유는 moves 는 불친절하게 1부터 시작하기 때문
                board[j][val1-1] = 0
                stack.pop()
                res += 2  #인형이 짝지어서 터지니까 2개가 터짐
                break
            else:
                stack.append(board[j][val1-1])
                board[j][val1-1] = 0  #이거하고 뽑은 인형을 영으로 해줘야 한다. 인형을 뽑았는데 있으면 안되자나
                break
    return res  # 인형을 뽑았으면 그거를 0으로 만들어야 하는걸 빼먹었어 !@! ! !! -2 로 하드코딩하면 무조건 오답이겠지
board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]
         ]
moves = [1,5,3,5,2,1,4]
print(solution(board,moves))