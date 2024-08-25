def solution(brown, yellow):
    answer = []
#     두 수를 더해야 총 타일의 개수가 되므로
    summ = brown + yellow
#     ㅈㅔㄱㅗㅂㄱㅡㄴ ㄲㅏㅈㅣ ㄷㅓㅎㅏㄴㄷㅏ.
    for width in range(3, int(summ ** 0.5)+1):
        if summ % width == 0:
            height = summ // width
            yellow1 = (width -2) * (height -2)
            
            if yellow1 == yellow:
                
                return [max(width, height), min(width, height)]

    return []