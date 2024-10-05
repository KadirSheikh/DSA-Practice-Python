import math

class Solution:
    def modInversionFLT(self, a, n):
        self.a = a
        self.n = n
        
        gcd = math.gcd(a, n)
        if gcd != 1:
            print("Modulo Inversion does not exists")
            return -1
            
        return pow(a, n - 2, n)
        
mySol = Solution()
ans = mySol.modInversionFLT(10, 17)
print(ans)