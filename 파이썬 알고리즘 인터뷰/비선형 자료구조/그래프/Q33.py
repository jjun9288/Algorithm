# 전화 번호 문자 조합

phone = {'1' : '',
         '2' : 'abc',
         '3' : 'def',
         '4' : 'ghi',
         '5' : 'jkl',
         '6' : 'mno',
         '7' : 'pqrs',
         '8' : 'tuv',
         '9' : 'wxyz',
         '0' : '+'
         }

digits = '23'
result = []

def dfs(index, path):
    if len(path) == len(digits):
        result.append(path)
    
    for i in range(index, len(digits)):
        for j in phone[digits[i]]:
            dfs(i + 1, path + j)
            
    return result
    
print(dfs(0,""))
    
    

