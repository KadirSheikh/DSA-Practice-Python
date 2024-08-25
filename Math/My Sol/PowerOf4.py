class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        self.n = n
        
        if n == 1 or n == 4:
            return True
            
        while n != 0:
            remainder = n / 4
            if remainder >= 4:
                n = remainder
            else:
                return False
                
            if n / 4 == 1:
                return True
            

======================================================================================

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        self.n = n
        
        if n < 0:
            return False
            
        while n != 0:
            if n % 4 == 0:
                n = n // 4
            elif n == 1:
                return True
            else:
                return False
                
            
mySol = Solution()
isPower = mySol.isPowerOfFour(16777216)

print(isPower)