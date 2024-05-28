hour, minute = map(int, input().split())
cooking_time = int(input())

cooking_hour = cooking_time // 60 #80/60 = 1
cooking_minute = cooking_time % 60  #80 % 60 = 20분


res_hour = hour + cooking_hour
res_minute = minute + cooking_minute

if res_minute >= 60:
    res_minute -= 60
    res_hour += 1
if res_hour >= 24:
    res_hour -= 24

print(res_hour, res_minute)