com = int(input())
network = int(input())

graph = [[] for _ in range(com + 1)]
for _ in range(network):
    a,b = list(map(int,input().split()))
    graph[a].append(b) #무방향 그래프
    graph[b].append(a)

visited=[0]*(com+1) # 방문한 컴퓨터인지 표시
def dfs(start):
    visited[start] = 1
    for adj in graph[start]:
        if visited[adj] == 0:
            dfs(adj)
dfs(1)
print(sum(visited)-1) # 처음부터 1번은 감염되어있었다
