class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.num = num
        
        hexDigits = "0123456789abcdef"
        result = ""
        
        if num == 0:
            return "0" 
        
        if num < 0:
            num = 2**32 + num
            
        while num > 0:
            remainder = num % 16
            result = hexDigits[remainder] + result
            num = num // 16
            
        return result