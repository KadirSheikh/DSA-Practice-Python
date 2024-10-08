class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.n = n
        
        countOfZero = 0
        
        while n != 0:
            countOfZero = countOfZero + (n // 5)
            n = n // 5
            
        return countOfZero
            