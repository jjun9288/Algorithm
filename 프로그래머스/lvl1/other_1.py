def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = []
    win, zeros = 0, 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                win += 1
        else:
            zeros += 1
    
    max = win + zeros
    answer.append(rank[max])
    min = win
    answer.append(rank[min])
    return answer