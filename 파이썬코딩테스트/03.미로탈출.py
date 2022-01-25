# bfs는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색합니다.
# 상하좌우로 연결된 모든 노드로의 거리가 1로 동일합니다.
# 따라서 (1,1) 지점부터 bfs를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있습니다.

from collections import deque

# N, M을 공백 기준으로 구분하여 입력받기
n, m = map(int, input().spilt())

# 2차원 리스트의 맵정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 4가지 방향정의 ( 상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.apped((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))
