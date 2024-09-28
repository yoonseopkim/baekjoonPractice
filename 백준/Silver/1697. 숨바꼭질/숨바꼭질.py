from collections import deque

def bfs(a,b):
    # a 가 수빈, b 가 동생

    # 최대값 제한을 걸어둔다.
    MAX = 100001
    #가장 빠른 시간->  bfs
    #수빈의 초기 위치, 시간을 0 으로 초기화
    queue = deque([(a, 0)])
    visited = [False] * MAX


    while queue:
        current, time = queue.popleft()
        # 동생을 찾았을경우
        if current == b:
            return time
        # 이동 반경 구하기
        for i in (current-1, current+ 1, current * 2):
        #그렇지 못할경우, 일단 방문 되었는지 안되어있는지 확인
            if 0 <= i < MAX and not visited[i]:
                visited[i] = True
                queue.append((i, time + 1 ))

a, b = map(int,input().split())
print(bfs(a, b))


    # 방문이 안되었는지는 알아야한다.

