s = input().strip()

count = 0

# 첫 번째 문자를 시작점으로 설정합니다.
current = s[0]

# 문자열의 두 번째 문자부터 마지막 문자까지 순회합니다.
for char in s[1:]:
    # 현재 문자와 다음 문자가 다른 경우 뒤집기 횟수를 하나 증가시킵니다.
    if current != char:
        count += 1
        current = char

# 총 뒤집기 횟수를 출력합니다.
print((count // 2) + (count % 2))
