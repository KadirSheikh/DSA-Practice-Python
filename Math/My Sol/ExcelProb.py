class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        num_to_letter = {
                1: 'A',
                2: 'B',
                3: 'C',
                4: 'D',
                5: 'E',
                6: 'F',
                7: 'G',
                8: 'H',
                9: 'I',
                10: 'J',
                11: 'K',
                12: 'L',
                13: 'M',
                14: 'N',
                15: 'O',
                16: 'P',
                17: 'Q',
                18: 'R',
                19: 'S',
                20: 'T',
                21: 'U',
                22: 'V',
                23: 'W',
                24: 'X',
                25: 'Y',
                26: 'Z'
            }
            
        
        colAlpha = ''
        while columnNumber != 0:
            columnNumber -= 1
            letter = int(columnNumber % 26) + 1
            colAlpha = num_to_letter[letter] + colAlpha
            columnNumber = columnNumber // 26
            
        return colAlpha