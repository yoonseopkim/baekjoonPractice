from collections import Counter
n = input()
# 짝수 2개 ㄱㅊ, 홀수 1, 짝수 1 ㄱㅊ, 홀수가 2개 이상이면 불가능함
a = Counter(n)
odd = 0
#  하나만 있는 단어를 나타냄
odd_word = ''
for word_type, word_cnt in a.items():
    if word_cnt % 2 != 0:
        odd_word = word_type
        odd += 1
        if odd > 1 :
            print("I'm Sorry Hansoo")
            exit()
res = []
#  단어 개수가 아니라 단어 자체를 뜻함
for word in sorted(a.keys()):
    word_cnt = a[word] // 2
    res += [word * word_cnt]

left_half = ''.join(res)
right_half = left_half[::-1]

if odd == 1:
    res = left_half + odd_word + right_half
else:
    res = left_half + right_half

print(res)