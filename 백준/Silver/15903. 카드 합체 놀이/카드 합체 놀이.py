import heapq
n, plus = map(int,input().split())
card = list( map(int,input().split()))
heapq.heapify(card)
for _ in range(plus):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    sumy = x+y
    heapq.heappush(card, sumy)
    heapq.heappush(card, sumy)

print(sum(card))

