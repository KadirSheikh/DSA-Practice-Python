class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.n = n
        
        if n <= 0:
            return 0
        
        a = 0
        b = 1
        
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        
        return b
        

mySol = Solution()

fibo = mySol.fib(0)

print(fibo)