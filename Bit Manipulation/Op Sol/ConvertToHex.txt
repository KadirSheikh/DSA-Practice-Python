class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.num = num
        result = ""
        
        if num == 0:
            return "0" 
        
        if num < 0:
            num = 2**32 + num
            
        while num != 0:
            remainder = num % 16
            num = num // 16
            
            if remainder >= 10:
                result += chr(remainder + 87)
            else:
                result += str(remainder)
            
        return result[::-1]