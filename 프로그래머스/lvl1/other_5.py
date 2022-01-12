def solution(nums):
    answer = 1
    pick_list, tmp = [], []
    pick = len(nums) // 2
    
    pick_list.append(nums[0])
    tmp.append(nums[0])
    for i in nums:
        if i not in pick_list:
            if len(pick_list) < pick:
                pick_list.append(i)
    while (len(pick_list) < pick):
        pick_list.append(nums[0])
    for i in pick_list:
        if i not in tmp:
            answer += 1
    return answer