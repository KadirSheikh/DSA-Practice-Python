class Solution:
    def isPrime(self, n):
        self.n = n
        
        if n <= 1:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        
        return True
            
            
        
    def primeRange(self,M,N):
        self.M = M
        self.N = N
        
        primeNo = []
        for i in range(M, N + 1):
            if self.isPrime(i):
                primeNo.append(i)
                
        return primeNo
        
mySol = Solution()
m = 1
n = 10
ans = mySol.primeRange(m, n)
print(ans)