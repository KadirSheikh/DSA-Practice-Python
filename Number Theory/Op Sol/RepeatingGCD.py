class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b) 
    
    def FindGcd(self, N, x, y):
        gcd_val = self.gcd(x, y)
        return str(N) * gcd_val  
           

mySol = Solution()
N = 2
x = 2
y = 3
MS = mySol.FindGcd(N, x, y)
print(MS)
