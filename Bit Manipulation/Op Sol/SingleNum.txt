class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        self.nums = nums

        singleNum = 0
        for i in nums:
            singleNum = singleNum ^ i

        return singleNum