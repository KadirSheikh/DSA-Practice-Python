class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        
        reverse = 0
        checkPalindrome = x
         
        x = abs(x)
        while x != 0:
            remainder = x % 10
            reverse = remainder + 10 * reverse
            x = x // 10
            
        return reverse == checkPalindrome and x >= 0
            