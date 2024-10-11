from collections import deque
import copy

#  처음부터 2면 감염된 장소라고 표시해두어야함
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_safe_area = 0

def spread_virus(temp_lab):
    """
   바이러스를 퍼뜨리는 함수
   :param temp_lab: 임시 연구소 상태
   :return: 안전 영역의 크기
   """

    queue = deque()

    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y  = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))
    safe_area = sum(row.count(0) for row in temp_lab )
    return safe_area

def build_wall(count):
    """
  벽을 세우는 함수 (재귀적으로 호출됨)
  :param count: 현재까지 세운 벽의 개수
  """
    global max_safe_area
    # 벽을 3개 세우고 바이러스 확산 시뮬레이션 시작
    if count == 3:
      temp_lab = copy.deepcopy(lab)
      safe_area = spread_virus(temp_lab)
      max_safe_area = max(safe_area, max_safe_area)
      return

#     벽을 세우는 모든 경우의 수 시도
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build_wall(count + 1)
                lab[i][j] = 0

build_wall(0)

print(max_safe_area)





