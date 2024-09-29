class Solution:
    def findGCD(self, A, B):
        self.A = A
        self.B = B
        
        if B == 0:
            return A
        
        return self.findGCD(B, A%B)
    
    def lcmAndGcd(self, A , B):
        self.A = A
        self.B = B
        
        gcd = self.findGCD(A, B)
        lcm = A * B // gcd
        
        return [lcm, gcd]
        

mySol = Solution()
num1 = 5
num2 = 10
MS = mySol.lcmAndGcd(num1, num2)
print(MS)