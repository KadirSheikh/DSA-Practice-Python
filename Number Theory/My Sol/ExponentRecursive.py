class Solution:
    def findExponent(self, a, b):
        self.a = a
        self.b = b
        
        if b == 0:
            return 1
        
        return a * self.findExponent(a, b-1)
        


mySol = Solution()
exponent = mySol.findExponent(2, 3)
print(exponent)