# 3) 음료수 얼려 먹기

from collections import deque

n, m = map(int, input().split())

info = []
for i in range(n):
    info.append(list(map(int, input())))

cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    info[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if info[nx][ny] == 0:
                DFS(nx, ny)

for i in range(n):
    for j in range(m):
        if info[i][j] == 0:
            DFS(i, j)
            cnt += 1
            
print(cnt)


