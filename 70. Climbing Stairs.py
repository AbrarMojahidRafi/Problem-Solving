class Solution:
  def climbStairs(self, n):
    count = 0 
    sum = 0 
    i = 0 
    while (i < n): 
      if sum == n: 
        count += 1 
        break 
      else: 
        sum += i
      i += 1 
    return count  
  

s = Solution()
print(s.climbStairs(3))