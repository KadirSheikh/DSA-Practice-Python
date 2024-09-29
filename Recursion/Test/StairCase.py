class Solution(object):
   def staircase(self, n, current=1):
       if current > n:
           return
       spaces = n - current
       hashes = current
       print(" "*spaces + "#"*hashes)
       self.staircase(n, current+1)

mySol = Solution()
n = 6
BS = mySol.staircase(n)
