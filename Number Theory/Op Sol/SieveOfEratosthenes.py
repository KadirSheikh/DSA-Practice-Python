class Solution:
    def isPrime(self, num):
        if num <= 1:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
        
    def sieveOfEratosthenes(self, N):
    	self.N = N
    	
    	primeNumber = []
    	for i in range(2, N+1):
    	    if self.isPrime(i):
    	        primeNumber.append(i)
    	        
    	return primeNumber
    	
    	
    	
mySol = Solution()
num1 = 9
MS = mySol.sieveOfEratosthenes(num1)
print(MS)