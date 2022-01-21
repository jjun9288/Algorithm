# 세 수의 합

# 1. 브루트포스 
nums = [-1, 0, 1, 2, -1, -4]

answer = []
tmp = []

for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                tmp.append(nums[i])
                tmp.append(nums[j])
                tmp.append(nums[k])
                answer.append(tmp)
                tmp = []
print(answer)

# 시간복잡도 O(n**3) 이 나온다. (타임아웃)

# 2. 투 포인터

answer = []
nums.sort()

for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    left, right = i+1, len(nums)-1
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            answer.append([nums[i], nums[left], nums[right]])
            
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
                
            left += 1
            right -= 1

print(answer) 

# 시간 복잡도를 O(n**2)으로 줄일 수 있다.