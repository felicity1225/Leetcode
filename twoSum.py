class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if nums[i] in d:
                return d[nums[i]],i
            d[a] = i
        
