from collections import deque

def sol(n,row):
    queue = deque([(0,0)])
    visited = set()
    visited.add((0,0))
    while queue:
        x,y = queue.popleft()
        jump = row[x][y]

        if jump == -1:
            return 'HaruHaru'


        nx, ny  = x + jump, y

        if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
            queue.append((nx,ny))
            visited.add((nx,ny))
        nx, ny  = x, y + jump

        if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
            queue.append((nx,ny))
            visited.add((nx,ny))
    return 'Hing'


n = int(input())
row = [list(map(int,input().split())) for _ in range(n)]
print(sol(n,row))