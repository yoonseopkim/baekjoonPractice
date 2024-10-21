def check_year(Y):
    if Y % 4 ==0 :
        if Y % 100 == 0:
            if Y % 400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
             


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
    check_year(Y)
    # 31일까지
    if M in (1, 3, 5, 7, 8,10,12):
        if 1<= D <=31:
            return True
        else:
            return -1
    elif M in (4,6,9,11):
        if 1<= D <=30:
            return True
        else:
            return -1  
    elif M == 2:
        # 윤년 
        if check_year(Y) == True:
            if 1<= D <=29:
                return True
            else:
                return -1
        # 윤년아님
        else:
            if 1<= D <=28:
                return True
            else:
                return -1            
        
    # 달이 이상할경우
    else:
        return -1  




def solution(Y,M,D):
    # 윤년부터 체크? 
    if okay_day(Y, M, D):
        return check_month(M)
    else:
        return None

Y, M , D = map(int,input().split())
print(solution(Y, M , D))