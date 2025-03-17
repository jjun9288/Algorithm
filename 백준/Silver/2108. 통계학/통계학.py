import sys
input = sys.stdin.readline

N = int(input())
nums = []
sum = 0
nums_dict = dict()

for _ in range(N):
    i = int(input())
    nums.append(i)
    sum += i
    if i not in nums_dict:
        nums_dict[i] = 1
    else:
        nums_dict[i] += 1
nums.sort()

print(round(sum / N))
print(nums[N//2])

freq = max(nums_dict.values())
freq_list = []
for key, value in nums_dict.items():
    if value == freq:
        freq_list.append(key)
if len(freq_list) == 1:
    print(freq_list[0])
else:
    print(sorted(freq_list)[1])

print(nums[-1]-nums[0])