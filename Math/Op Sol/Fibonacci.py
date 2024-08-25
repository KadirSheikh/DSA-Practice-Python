class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.n = n
        
        if n == 0 or n == 1:
            return n
            
        return self.fib(n - 1) + self.fib(n - 2)
        

mySol = Solution()

fibo = mySol.fib(3)

print(fibo)