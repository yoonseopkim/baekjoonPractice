from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([(0,0,1)])
    visited = set([(0,0)])

    while queue:
        x,y, dist = queue.popleft()
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <=ny < m and (nx,ny) not in visited and maps[nx][ny]== 1:
                queue.append((nx,ny,dist + 1))
                visited.add((nx,ny))
        
    return -1