import heapq
import sys

input =sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        # 아무것도 없을시 예워처리
        if not heap:
            print(0)
        else:
        # 최대힙이므로 가장 큰값을 먼저 반납 해야할듯?
            print(-heapq.heappop(heap))

    # 다른 숫자일경우 그거를 힙에 넣는다. , 최대힙이므로 뒤집어서 넣어야 함.
    else:

        heapq.heappush(heap, -cmd)

