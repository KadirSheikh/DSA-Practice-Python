class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.digits = digits
        digitStr = ''
        newDigits = []
        for i in digits:
            digitStr += str(i)
        
        digitInt = int(digitStr)
        incrementDigit = str(digitInt + 1)
        
        for j in incrementDigit:
            newDigits.append(int(j))
            
        print(newDigits)
        return newDigits
        

        
mySol = Solution()
mySol.plusOne([1, 9, 99])