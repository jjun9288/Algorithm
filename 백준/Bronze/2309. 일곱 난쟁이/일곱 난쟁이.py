import sys
from itertools import combinations

input = sys.stdin.readline

heights = []
for _ in range(9):
    heights.append(int(input()))

heights.sort()

for combination in combinations(heights, 7):
    tmp = 0
    for i in combination:
        tmp += i
    if tmp == 100:
        answer = list(combination)

for a in answer:
    print(a)