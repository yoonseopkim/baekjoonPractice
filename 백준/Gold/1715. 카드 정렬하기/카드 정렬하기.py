# 그리디 조합은 시간초과, 최소 힙
import heapq
n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)
total = 0
while len(cards) > 1:
    first_card = heapq.heappop(cards)
    second_card = heapq.heappop(cards)
    cards_sum = first_card + second_card
    total += cards_sum
    heapq.heappush(cards, cards_sum)
print(total)
