class Solution:
    def gcd(self, a, b):
        self.a = a
        self.b = b
        while b:
            a, b = b, a % b
        return a
	
	def FindGcd(self, N, x, y):
		self.N = N
		self.x = x
		self.y = y
		
		A = str(N) * x
		B = str(N) * y
	
		gcd = self.gcd(int(A), int(B))
		return gcd           

mySol = Solution()
N = 2
x = 2
y = 3
MS = mySol.FindGcd(N, x, y)
print(MS)