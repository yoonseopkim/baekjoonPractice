com = int(input())
network = int(input())

graph = [[] for _ in range(com + 1)]
for _ in range(network):
    a,b = list(map(int,input().split()))
    graph[a].append(b) #무방향 그래프
    graph[b].append(a)

visited = [False] * (com + 1)
def dfs(start):
    infected = 0
    visited[start] = True
    for adj in graph[start]:
        if not visited[adj]:
            infected += dfs(adj)
    return infected + 1

print(dfs(1)-1)
