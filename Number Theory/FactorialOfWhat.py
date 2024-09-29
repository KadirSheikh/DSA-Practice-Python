class Solution:
    def isFactorial (self, num):
        self.num = num
        if num == 0 or num == 1:
            return 0
        
        start = 2
        
        while(num > 1):
            if num % start == 0:
                num = num // start
                start += 1
            else:
                return 0
                
        return start - 1
    	
    	
mySol = Solution()
num = 6
MS = mySol.isFactorial(num)
print(MS)