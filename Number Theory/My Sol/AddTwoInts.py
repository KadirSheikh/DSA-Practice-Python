class Solution:
	def addTwoInt(self, num1, num2):
	    self.num1 = num1
	    self.num2 = num2
	    
	    while num2:
	        carry = num1 & num2
	        print("carry", carry)
	        num1 ^= num2
	        print("num1", num1)
	        num2 = carry << 1
	        print("num2", num2)
	    return num1

mySol = Solution()
num1 = 10
num2 = 23
MS = mySol.addTwoInt(num1, num2)
print(MS)