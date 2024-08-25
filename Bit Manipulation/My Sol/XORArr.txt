class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [0] * n
        i = 0
        xornum = 0
        for i in range(0, n):
           nums[i] = start + 2 * i
           
        for i in nums:
            xornum = xornum ^ i
            
        return xornum