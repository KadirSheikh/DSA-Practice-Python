class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        self.n = n
        print("####", 1 % 4)
        while n % 4 == 0:
            print("Divide", n)
            n = n // 4
            print("Mod Divide", n % 4)
            
        return n == 1
            
            
mySol = Solution()
isPower = mySol.isPowerOfFour(64)

print(isPower)