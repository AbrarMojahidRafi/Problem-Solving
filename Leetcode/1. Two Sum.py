# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             j=i+1
#             if nums[i]+nums[j]==target and j<len(nums):
#                 return [i,j]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            var = nums[i]
            for j in range(len(nums)):
                if var + nums[j]==target and i!=j:
                    lst=list()
                    return i,j
s = Solution()
print(s.twoSum([2,7,11,15], 9))