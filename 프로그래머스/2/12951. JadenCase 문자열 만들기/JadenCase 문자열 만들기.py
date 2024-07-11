def solution(s):
    s = s.lower() #일단 전부 소문자로 바꾸기
    li_s = s.split(" ")  #그리고 공백 기준으로 나눠서 첫글자만 대문자로 바꿔ㅜ저야함

    a = len(li_s)
    tmp = []
    for i,val in enumerate(li_s):     
        if val: 
            a = val[0].upper() + val[1:]
            res = "".join(a)
            
        else: #빈 문자열 처리를 해줘야함 예위처리
            res =""
        tmp.append(res)
    # tmp1 = print(*tmp)
    tmp1 = ' '.join(map(str, tmp))
    return tmp1   #이미 문자열
    # print(tmp1)
    # answer = f'"{tmp1}"'
    # return answer


    