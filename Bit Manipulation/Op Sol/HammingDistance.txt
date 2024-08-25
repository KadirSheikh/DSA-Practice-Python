class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalHD = 0
        n = len(nums)
        for bit in range(32):
            totalOne = 0
            for num in nums:
                if num & (1 << bit):
                    totalOne += 1
            totalZero = n - totalOne
            totalHD += totalOne * totalZero
        return totalHD