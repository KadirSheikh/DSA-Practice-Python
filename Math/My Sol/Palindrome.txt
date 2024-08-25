class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        
        reverse = 0
        sign = '-' if x < 0 else ''
        checkPalindrome = x
         
        x = abs(x)
        while x != 0:
            remainder = x % 10
            reverse = remainder + 10 * reverse
            x = x // 10
            
        if str(checkPalindrome)  == str(reverse) + sign:
            return True
            
        return False