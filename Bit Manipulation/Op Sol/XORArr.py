class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [start + 2 * i for i in range(n)]
        xornum = nums[0]
        for i in nums[1:len(nums)]:
            xornum = xornum ^ i 
        return xornum 
 