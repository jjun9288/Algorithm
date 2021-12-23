# 실전 문제 ) 게임 개발
'''
남 : 2 : 열 + 1
북 : 0 : 행 - 1
동 : 1 : 열 - 1
서 : 3 : 행 + 1

모두 가봤다면 
    행 - 1
그마저도 바다면
    제자리
    
'''

n, m = map(int, input().split())               # map 크기 (n x m)
r, c, i = map(int, input().split())            # (x,y), 캐릭터 방향
game = []

for i in range(n):
    game[i] = [0]*m