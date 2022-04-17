arr = [1,None,None,3,None,None,5,None]

def solution(array):
    valid = 0            
    res = []                 
    for i in nums: 
        if i is not None:    
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

solution(arr)