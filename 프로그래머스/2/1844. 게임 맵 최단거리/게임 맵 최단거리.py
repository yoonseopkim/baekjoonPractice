from collections import deque
def solution(maps):
#     초기값 설정
    n, m  = len(maps), len(maps[0])
    answer = 0
#     x,y 방향을 정하는 것
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
#     이동할때마다 좌표와 거리 누적합 담는다.
    queue = deque([(0,0,1)])
# 방문 했는지 알려주는 좌표값을 집합으로 담는다
    visited = set([(0,0)])
    while queue:
        x,y,dist=queue.popleft()
#         목적지에 도달 했을 경우
        if x == n-1 and y == m-1:
            return dist
        
#         사방으로 이동을 시도해본다,
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx,ny) not in visited:
                queue.append((nx,ny, dist+1))
                visited.add((nx, ny))

            
    return -1