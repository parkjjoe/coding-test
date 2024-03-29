import sys

n, m = map(int, sys.stdin.readline().split())

data = [] # 초기 맵
temp = [[0] * m for _ in range(n)] # 벽 설치한 뒤의 맵

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

# 4가지 이동 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS로 바이러스가 퍼지게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m: # 상하좌우 중 바이러스가 퍼질 수 있는 경우
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치, 재귀적 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS로 벽을 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result

    if count == 3: # 벽이 3개 설치되면
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 벽 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
