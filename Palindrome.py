s = "civic"
s1 = "homsi"
def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True
    return s == s[::-1]
  
print(solution(s)) #TRUE
print(solution(s1)) #FALSE