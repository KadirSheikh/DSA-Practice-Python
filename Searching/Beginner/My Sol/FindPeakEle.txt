class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                return i
                
        return 0