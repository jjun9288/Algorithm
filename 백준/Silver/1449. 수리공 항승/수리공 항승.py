import sys
input = sys.stdin.readline
N, L = map(int, input().split())

holes = [False] * 1001
for i in map(int, input().split()):
    holes[i] = True

cnt = 0
x = 0

while x < 1001:
    if holes[x] == True:
        cnt += 1    # 테이프 1회 사용
        x += L      # 테이프 길이 구간에 있는 구멍 모두 메꾸므로 pass
    else:
        x += 1  # 테이프 사용이 끝난 다음 구간부터 다시 확인

print(cnt)