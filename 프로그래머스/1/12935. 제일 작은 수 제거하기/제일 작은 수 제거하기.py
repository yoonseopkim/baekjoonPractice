def solution(arr):
    answer = []
    miny = min(arr)
    for a in arr:
        if len(arr) == 1:
            return [-1]
        
        elif a != miny:
            answer.append(a)
            
    return answer