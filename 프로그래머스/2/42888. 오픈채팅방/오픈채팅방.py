def solution(record):
    # 문제분석
    # 기존 채팅방에 있던 내용도 바뀐 닉네임으로 변경되는걸 알아야함
    #중복 닉네임 허용
    # 유저아이디로 구분함
    # 입력값이 백만이라서 이중 포문은 생각해볼것

    # 알고리즘
    # 해시를 이용하면 키 : 값으로 받기 때문에 좋을듯. 유저 아이디 : 닉네임

    #엣지 케이스
    #없음
    hash = {}
    actions = []

    for r1 in record:
        r = r1.split()
        cmd, uid = r[0], r[1]

        if cmd in ['Enter','Change']:
            nickname = r[2]
            hash[uid] = nickname

        if cmd != 'Change':
            actions.append((cmd,uid))

        answer = []
    for cmd, uid in actions:
        if cmd == 'Enter':
            answer.append(f'{hash[uid]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(f'{hash[uid]}님이 나갔습니다.')

    return answer