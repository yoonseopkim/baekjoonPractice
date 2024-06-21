def solution(n, words):
    answer = []
    game = [] #이미 말한거 넣는거 방지
    for i, val in enumerate(words):
        if not game:  #아무것도 없으면
            game.append(val)
            continue
        elif game[-1][-1] != val[0]:
            answer.append((i % n) + 1)  #순서와 몇번쨰로 틀렸는지를
            answer.append((i // n) + 1)  #순서와 몇번쨰로 틀렸는지를
            break
        elif val in game: # 이미 말한 단어 말했을경우
            answer.append((i % n) + 1)  #순서와 몇번쨰로 틀렸는지를
            answer.append((i // n) + 1)  #순서와 몇번쨰로 틀렸는지를
            break
        game.append(val)
    if len(game) == len(words):
        answer = [0,0]
    return answer