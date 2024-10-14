from itertools import combinations
from collections import deque

board = [input().strip() for _ in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(comb):
    visited = set()
    queue = deque([comb[0]])
    visited.add(comb[0])

    while queue:
        #  7을 달성했을경우 경우의 수를 리턴한다 ,
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (nx,ny) in comb and (nx,ny) not in visited:
                queue.append((nx,ny))
                visited.add((nx,ny))
    return len(visited) ==7

def check_valid(comb):
    s_count = sum(1 for x,y in comb if board[x][y] == 'S')
    return s_count >= 4 and bfs(comb)

positions = [(i,j) for i in range(5) for j in range(5)]
count = sum(1 for comb in combinations(positions, 7 ) if check_valid(comb))

print(count)
