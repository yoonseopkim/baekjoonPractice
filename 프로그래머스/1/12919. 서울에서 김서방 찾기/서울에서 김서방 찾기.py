def solution(seoul):
    answer = ''
    for i,val in enumerate(seoul):
        if val =='Kim':
            answer = '김서방은 '+str(i)+ '에 있다'
            return answer