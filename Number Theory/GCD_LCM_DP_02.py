class Solution:
    # Optimized GCD using Euclidean algorithm
    def findGcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    # Optimized LCM using the relation LCM(a, b) = (a * b) / GCD(a, b)
    def findLcm(self, a, b):
        return abs(a * b) // self.findGcd(a, b)
    
    # Function to find the required value
    def findValue(self, x, y, z):
        lcm_xy = self.findLcm(x, y)
        lcm_xz = self.findLcm(x, z)
        return self.findGcd(lcm_xy, lcm_xz)
        
        
        
mySol = Solution()
x = 15
y = 20
z = 100
ans = mySol.findValue(x, y, z)
print(ans)