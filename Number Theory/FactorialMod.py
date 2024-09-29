class Solution:
    def factorialMod(self, n, a):
        self.n = n
        self.a = a
        
        result = 1
        
        for i in range(2, n + 1):
            result = (result * i) % a
        return result

mySol = Solution()
ans = mySol.factorialMod(100, 10)
print(ans)