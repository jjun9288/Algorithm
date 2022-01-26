# 유기농 배추

n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x,y):
    farm[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if farm[nx][ny] == 1:
                DFS(nx,ny)

for i in range(n):
    cnt = 0
    n, m, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    
    for j in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1
        
    for a in range(n):
        for b in range(m):
            if farm[a][b] == 1:
                DFS(a,b)
                cnt += 1
        
    print(cnt)