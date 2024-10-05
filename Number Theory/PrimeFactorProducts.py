class Solution:
    def primeProduct(self, N):
        self.N = N
        product = 1
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                product *= i
                while N % i == 0:
                    N = N // i
        
        if N > 1:
            product *= N
            
        return product
        
mySol = Solution()
x = 5
ans = mySol.primeProduct(x)
print(ans)