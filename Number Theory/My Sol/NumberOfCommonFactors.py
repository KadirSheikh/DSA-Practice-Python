class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        self.a = a
        self.b = b
        
        noOfFactors = 1
        minNum = a
        
        if a == b:
            minNum = a
            
        if b < a:
            minNum = b
        
        for i in range(2, minNum+1):
            if (a % i == 0) and (b % i == 0):
                noOfFactors += 1
                
        print("Number of common factors", noOfFactors)
        return noOfFactors    
mySol = Solution()
mySol.commonFactors(12, 6)