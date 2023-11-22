class Solution:
    def searchInsert(self, nums_int, target_int):
        pointer1 = 0
        index = 0
        loopCounter = 0
        while (loopCounter < len(nums_int)):
            if nums_int[loopCounter] < target_int:
                index += 1 
            else:
                return index
            loopCounter += 1
        return index
      
      
s = Solution()
print(s.searchInsert([1,3,5,6], 5))