class Solution:
  def climbStairs(self, n):
    count = 0 
    for _ in range(n): 
      sum = 0 
      for i in range(n):
        # print(i)
        if sum == n:
          count += 1
          break
        else: 
          sum += i
          i += 1
    return count
  

s = Solution()
print(s.climbStairs(3))