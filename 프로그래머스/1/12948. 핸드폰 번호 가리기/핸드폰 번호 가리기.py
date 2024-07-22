def solution(phone_number):
    a = len(phone_number)
    b = phone_number[-4:]
    answer = ''
    for i in range(a-4):
        answer += '*'
    answer += b
    return answer