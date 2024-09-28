class Solution:
    def factorProduct(self,N):
        self.N = N
        product = 1
        mod = 1000000007
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                if N // i == i:
                    product = (product * i) % mod
                else:
                    product = (product * i * N // i) % mod
                    
        return product 
                    

mySol = Solution()
num1 = 25
MS = mySol.factorProduct(num1)
print(MS)
