class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1
      
      
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))