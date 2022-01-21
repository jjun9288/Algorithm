# 두 수의 합

# 1. 브루트 포스

def solution(nums, target):
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(solution([2,7,11,15], 9))

# 이렇게 하면 시간복잡도가 O(n**2)이 된다.

# 2. 첫 번째 수를 뺀 결과 키 조회

def solution(nums, target): 
    answer = []
    temp = {}
    
    for i, num in enumerate(nums):
        temp[num] = i
    
    for i, num in enumerate(nums):
        if target - num in temp and i != temp[target-num]:
            return[i, temp[target-num]]

print(solution([2,7,11,15], 9))

# 시간복잡도가 전체적으로 O(n)이 된다.

