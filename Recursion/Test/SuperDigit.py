class Solution(object):
    def calSum(self, con):
        self.con = con
        sum = 0
        for i in con:
            sum += int(i)
        return str(sum)
            
        
    def superDigit(self, n, k):
        initial_sum = self.calSum(n)
        summ = str(int(initial_sum) * k)
        if len(summ) == 1:
            return int(summ)
        
        return self.superDigit(summ, 1)

mySol = Solution()
n = '148'
k = 3
BS = mySol.superDigit(n, k)
print("Ans", BS)
