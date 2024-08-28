from collections import deque
def solution(maps):
#     bfs
    n = len(maps)  #행의 개수
    m = len(maps[0]) #열의 개수
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 처음 시작지점으로 초기화
    queue = deque([(0,0,1)])
    # 방문여부를 말하는 것
    visited = set([(0,0)])
    while queue:
        x,y,distance = queue.popleft()
#         목적자에 도척
        if x == n -1 and y == m -1:
            return distance
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx,ny) not in visited:
                queue.append((nx,ny,distance+1))
                visited.add((nx,ny))

    return -1