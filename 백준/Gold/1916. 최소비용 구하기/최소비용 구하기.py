# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
#
# 입력
# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
#
# 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
#


#최소비용과 가중치 -> 다익스트라 써야할그ㅛ
#우선순위 큐 쓰자
import heapq
def diek(n, m, graph, start_city, end_city):
    # inf 로 초기화 해주자.
    dis = [float('inf')] * (n+1)
    dis[start_city] = 0
    heap = []
#     처음애는 초기값을 넣어줘야 한다., 가중치와 , 마지막 방문 녿,
    heapq.heappush(heap, (0, start_city))
    while heap:
        dist, node = heapq.heappop(heap)

        if node == end_city:  # 목적지에 도달하면 최단 거리 반환
            return dist

        if dist > dis[node]:  # 이미 처리된 노드라면 스킵
            continue

#         포문이 들어가야 하나?
        for curr_node, curr_dist in graph[node]:
            cost = curr_dist + dist
            if cost < dis[curr_node]:
                dis[curr_node] = cost
                heapq.heappush(heap,(cost, curr_node))




n =int(input())
m =int(input())
graph = [[] for i in range(n+1)]
for _ in range(m):
    start, end, bus_dis = map(int,input().split())
    # 도착도시와 가중치(버스 비용) 을 튜플에 묶어 넣는다
    graph[start].append((end,bus_dis))
start_city, end_city = map(int,input().split())

print(diek(n,m,graph,start_city,end_city))
# print(heap[1])
# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
#
# 예제 입력 1

# 예제 출력 1
# 4