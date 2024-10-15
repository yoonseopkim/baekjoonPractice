from itertools import permutations

def solution(k, dungeons):
    max_explored = 0
    
#     모든 가능한 던전탐험순서 생성
    for p in permutations(dungeons):
        current_k = k 
        explored = 0
        
#         현재 순열에 따라 던전 탐험
        for min_required, cost in p:
            if current_k >= min_required:
                current_k -= cost
                explored += 1
            else:
                break
                
            max_explored = max(max_explored, explored)
    
    return max_explored