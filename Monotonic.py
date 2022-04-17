A = [1,1,2,3,7]
B = [6, 5, 4, 4] 
C = [1,1,1,3,3,4,3,2,4,2]

def Monotonic(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(Monotonic(A)) 
print(Monotonic(B)) 
print(Monotonic(C)) 