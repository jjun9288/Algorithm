# 실전 문제 ) 왕실의 나이트

dx = [2, 2, -2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

a = input()

cnt = 0

for i in range(8):
    
    row = int(a[1])
    col = int(ord(a[0])) - int(ord('a')) + 1
    row += dx[i]
    col += dy[i]
    
    if row >= 1 and row <= 8 and col >= 1 and col <= 8:
        cnt += 1
        
print(cnt)