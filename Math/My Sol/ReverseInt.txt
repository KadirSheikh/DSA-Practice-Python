class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        
        reverseInt = 0
        wasNegative = x
        if x < 0:
            x = x * (-1)
        
        for i in range(len(str(x))):
            remainder = x % 10
            reverseInt = remainder + reverseInt * 10
            x = x // 10
        
        if reverseInt < -2**31 or reverseInt > 2**31 - 1:
            return 0
        
        if wasNegative < 0:
            return reverseInt * (-1)
            
        return reverseInt