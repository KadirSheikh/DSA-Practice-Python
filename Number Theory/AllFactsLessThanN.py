class Solution:
    def findFact(self, n):
        fact = 1
        for i in range(1, n + 1):  
            fact *= i
        return fact
    

    def factorialNumbers(self, n):
        facts = []
        i = 1
        
        while True:
            if self.findFact(i) > n:
                break
            facts.append(self.findFact(i))
            i += 1
            
            
        return facts
        
mySol = Solution()
x = 6
ans = mySol.factorialNumbers(x)
print(ans)