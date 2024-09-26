from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # 방향을 정해주는 함수가 필요하다. 사방으로 이동할수 없으므로 코드만으로는
    dx =[-1,1,0,0]
    dy = [0,0,-1,1]
    #시작 위치가 0,0 이라고 했으므로 그리고 dist는 1부터 시작이므로 초기화를 이렇게 해준다.
    queue = deque([(0,0,1)])
    #방문여부를 표시하는게 필요. 안그럼 같은곳을 또 방문할수도 있으므로, 나중에 한번에 비교가 필요할수 있으므로 튜플로 묶어둔다.
    visited = {(0,0)}
    while queue:
        x,y,dist = queue.popleft()
        if x == n-1 and y == m-1:
            return dist
        
        #dx, dy 를 따라서 이동해보는 과정이 필요하다. 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 경로에 따라서 이동을 할수 있으면 하고, 안되면 막는다. 0이면 벽이고, 맵의 안에서만 이동 가능하며, 방문되지 않았어야 한다.
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx,ny) not in visited:
                queue.append((nx,ny,dist+1))
                visited.add((nx,ny))

    # 다 안될때
    return -1