import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key = lambda meetings : (meetings[1], meetings[0]))

cnt = 1
final = meetings[0][1]
for i in range(1, N):
    if meetings[i][0] >= final:
        final = meetings[i][1]
        cnt += 1

print(cnt)