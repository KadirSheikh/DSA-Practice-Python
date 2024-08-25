class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        self.num = num
        
        minSum = []
        dividedBy = 10

        for i in range(1, len(str(num))):
            remainder = num % dividedBy
            remaining = num // dividedBy
            dividedBy = dividedBy * 10
            reversed_remainder = int(str(remainder)[::-1])
            reversed_remaining = int(str(remaining)[::-1]) 

            if remainder == reversed_remainder:
                summ1 = remainder + remaining
                minSum.append(summ1)
                summ2 = remainder + reversed_remaining
                minSum.append(summ2)
                
            if remaining == reversed_remaining:
                summ1 = remaining + remainder
                minSum.append(summ1)
                summ2 = remaining + reversed_remainder
                minSum.append(summ2)
                
                
            if remainder != reversed_remainder:
                summ1 = remainder + remaining
                minSum.append(summ1)
                summ11 = remainder + reversed_remaining
                minSum.append(summ11)
                
                summ2 = reversed_remainder + remaining
                minSum.append(summ2)
                summ22 = reversed_remainder + reversed_remaining
                minSum.append(summ22)
                
                
        return min(set(minSum))

mySol = Solution()

minFourDigitSum = mySol.minimumSum(4009)

print(minFourDigitSum)