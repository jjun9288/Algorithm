# 부품 찾기

n = int(input())
me = list(map(int, input().split()))

m = int(input())
you = list(map(int, input().split()))

me.sort()

answer = []

def bs(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    
        if array[mid] == target:
            return mid
    
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
        
        return None
    
        

    
for i in you:
    result = bs(me, i, 0, m-1)
    
    if result == None:
        answer.append('no')
    else:
        answer.append('yes')
        
for i in answer:
    print(i, end = ' ')