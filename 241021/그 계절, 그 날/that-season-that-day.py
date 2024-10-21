def check_year(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True  # 400의 배수인 경우 윤년
            else:
                return False  # 100의 배수지만 400의 배수가 아닌 경우 평년
        else:
            return True  # 4의 배수이면서 100의 배수가 아닌 경우 윤년
    else:
        return False  # 4의 배수가 아닌 경우 평년
             


def check_month(M) :
    # 모든 조건이 맞을때 비로소 달을 내줘야함
    
    if 3<=M <=5:
        return 'Spring' 
    elif 6<= M <= 8:
        return 'Summer' 
    elif 9<= M <= 11:
        return 'Fall'   
    elif M == 12 or M== 1 or M==2:
        return 'Winter'   
    else:
        return -1   
    
def okay_day(Y, M, D):
    if M in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= D <= 31
    elif M in (4, 6, 9, 11):
        return 1 <= D <= 30
    elif M == 2:
        return 1 <= D <= 29 if check_year(Y) else 1 <= D <= 28
    else:
        return False




def solution(Y,M,D):
    # 윤년부터 체크? 
    if okay_day(Y, M, D):
        return check_month(M)
    else:
        return -1

Y, M , D = map(int,input().split())
print(solution(Y, M , D))