class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        
        start = 0
        end = x
        ans = 0

        if x == 0:
            return ans

        while start <= end:
            mid = (start + end) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return ans