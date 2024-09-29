class Solution:
    def findExponent(self, a, b):
        self.a = a
        self.b = b
        
        if b == 0:
            return 1
        elif b % 2 == 0:
            half_even_exponent = self.findExponent(a, b // 2)
            return a * half_even_exponent * half_even_exponent
        else:
            half_odd_exponent = self.findExponent(a, (b-1) // 2)
            return a * half_odd_exponent * half_odd_exponent

mySol = Solution()
exponent = mySol.findExponent(2, 3)
print(exponent)