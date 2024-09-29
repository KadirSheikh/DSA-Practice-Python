class Solution:
    def extendedGCD(self, a, b):
        self.a = a
        self.b = b
        
        if a == 0:
            return b, 0, 1
            
        gcd, x1, y1 = self.extendedGCD(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
        
    def modInversion(self, a, n):
        self.a = a
        self.n = n
        
        gcd, x, y = self.extendedGCD(a, n)
        if gcd != 1:
            return -1
            
        return x % n
        
mySol = Solution()
ans = mySol.modInversion(10, 17)
print(ans)