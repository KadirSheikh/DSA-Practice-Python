class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        
        start = 0
        end = x
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid * mid < x:
                start = mid + 1
            elif mid * mid > x:
                end = mid - 1
            else:
                return mid
        
        return end
        
mySol = Solution()
sqrt = mySol.mySqrt(10)

print(sqrt)