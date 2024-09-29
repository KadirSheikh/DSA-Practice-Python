class Solution:
    def addTwoInt(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
        if num2 == 0:
            return num1
        return self.addTwoInt(num1 ^ num2, (num1 & num2) << 1)

mySol = Solution()
num1 = 10
num2 = 23
MS = mySol.addTwoInt(num1, num2)
print(MS)
