n, m = map(int, input().split())
coin = [list(map(int, list(input().split()))) for _ in range(n)]
cnt = 0

def flip(x,y):
    for i in range(x+1):
        for j in range(y+1):
            coin[i][j] = 1 - coin[i][j]

for i in reversed(range(n)):
    for j in reversed(range(m)):
        if coin[i][j] == 1:
            cnt += 1
            flip(i,j)
            
print(cnt)
