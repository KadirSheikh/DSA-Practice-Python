class Solution:
    def findPrimeFactors(self, n):
        self.n = n
        
        factor = 2
        allFacors = []
        while n > 1:
            if n % factor == 0:
                allFacors.append(factor)
                n = n // factor
            factor += 1
            
        return allFacors    
            
    def primeProduct(self, N):
        self.n = n
        
        productFactor = 1
        
        for i in self.findPrimeFactors(N):
            productFactor *= i
        
        return productFactor
        
        
mySol = Solution()
n = 5
ans = mySol.primeProduct(n)
print(ans)