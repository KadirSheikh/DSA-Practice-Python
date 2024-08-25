class Solution(object):
    def reverse(self, s):
        str = ""
        for i in s:
            str = i + str
        return str
        
    def convertToNumber(self, columnTitle):
        """
        :type columnNumber: int
        :rtype: str
        """
        num_to_letter = {
                'A': 1,
                'B': 2,
                'C': 3,
                'D': 4,
                'E': 5,
                'F': 6,
                'G': 7,
                'H': 8,
                'I': 9,
                'J': 10,
                'K': 11,
                'L': 12,
                'M': 13,
                'N': 14,
                'O': 15,
                'P': 16,
                'Q': 17,
                'R': 18,
                'S': 19,
                'T': 20,
                'U': 21,
                'V': 22,
                'W': 23,
                'X': 24,
                'Y': 25,
                'Z': 26
            }
        
        total = 0
        rev = self.reverse(columnTitle)
        
        for i in range(len(rev)):
            total += num_to_letter[rev[i]] * (26**i)
        
        return total

mySol = Solution()
title = "ZY"
numberOfArr = mySol.convertToNumber(title)
print(numberOfArr)