class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        add = 0        
        for i in range(1, len(str(n)) + 1):
            if i % 2 == 1:
                add = add + int(str(n)[i-1])
            else:
                add = add - int(str(n)[i-1])
            
        return add