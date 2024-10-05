class Solution(object):
    def checkPalindromeRecursion(self, value, i):
        """
        :type n: int
        :rtype: int
        """
        self.value = value
        n = len(value)
        
        if i >= n // 2:
            return True
        
        if value[i] != value[n - 1 - i]:
            return False
            
        return self.checkPalindromeRecursion(value, i + 1)

        
mySol = Solution()
sample_str = "abbcecbba"
i = 0
ans = mySol.checkPalindromeRecursion(sample_str, i)
print("ans", ans)