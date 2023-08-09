com = int(input())
network = int(input())

graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)

for _ in range(network):
    n,m = list(map(int,input().split()))
    # 그래프선언, 양방향그래프

    graph[n].append(m)  # 양방향 그래프
    graph[m].append(n)

def dfs(start):
    visited[start] = True
    infected = 1
    for adj in graph[start]:
        if not visited[adj]:
            infected += dfs(adj)
    return infected
print(dfs(1)-1)