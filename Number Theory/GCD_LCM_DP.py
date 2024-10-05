class Solution:
    def findGcd(self, a, b):
        self.a = a
        self.b = b
        smaller = min(a, b)
        for i in range(smaller, 0, -1):
            if a % i == 0 and b % i == 0:
                return i  
            
    def findLcm(self, a , b):
        self.a = a
        self.b = b
        larger = max(a, b)
        
        while True:
            if larger % a == 0 and larger % b == 0:
                return larger
            larger += 1
        
    def findValue(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        return self.findGcd(self.findLcm(x, y), self.findLcm(x, z))
        
        
        
mySol = Solution()
x = 15
y = 20
z = 100
ans = mySol.findValue(x, y, z)
print(ans)