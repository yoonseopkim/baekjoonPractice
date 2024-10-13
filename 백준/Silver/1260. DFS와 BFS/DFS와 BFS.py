from collections import deque

#     스택 자료구조 사용
def dfs(graph, v , visited):
    visited[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i , visited)

def bfs(graph, start , visited):
#     큐를 사용한다
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#  입출력
n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a , b = map(int,input().split())
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# print(graph)
visited = [False] * (n + 1)
dfs(graph, v , visited)
print()

visited = [False] * (n + 1)
bfs(graph, v , visited)

