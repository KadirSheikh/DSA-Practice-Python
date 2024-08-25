class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.n = n
        
        countOfZero = 0
        powerOfFive = 5
        
        
        while n // powerOfFive > 0:
            countOfZero = countOfZero + n // powerOfFive
            powerOfFive = powerOfFive * 5
            
        return countOfZero