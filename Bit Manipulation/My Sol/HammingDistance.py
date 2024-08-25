Working:

class Solution(object):
    def findHammingDistance(self, num1, num2):
        count = 0
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                count += 1
        
        return count
            
        
    def modifyBinArr(self, maxLen, binArr):
        for i in range(len(binArr)):
            if len(binArr[i]) == maxLen:
                continue
            zerosToAdd = maxLen - len(binArr[i])
            binArr[i] = '0' * zerosToAdd + binArr[i]
            
        return binArr
        
    def convertToBinary(self, num):
        if num == 0:
            return '0'
        
        binaryNo = ''
        while num != 0:
            rem = num % 2
            binaryNo = str(rem) + binaryNo
            num = num // 2
        return binaryNo
        
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        binaryArr = []
        totalHD = 0
        
        for i in nums:
            binaryNum = self.convertToBinary(i)
            binaryArr.append(binaryNum)
        
        longest_string = max(binaryArr, key=len)
        maxLenInArr = len(longest_string)
        modifiedBinaryArr = self.modifyBinArr(maxLenInArr, binaryArr)
    
        for i in range(maxLenInArr-1, -1, -1):
            countOne = 0
            for j in modifiedBinaryArr:
                if j[i] == '1':
                    countOne += 1
                countZero = len(nums) - countOne 
            totalHD += countOne * countZero
                    
        return totalHD



========================================================================================


TLE ERROR:

class Solution(object):
    def findHammingDistance(self, num1, num2):
        count = 0
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                count += 1
        
        return count
            
        
    def modifyBinArr(self, maxLen, binArr):
        for i in range(len(binArr)):
            if len(binArr[i]) == maxLen:
                continue
            zerosToAdd = maxLen - len(binArr[i])
            binArr[i] = '0' * zerosToAdd + binArr[i]
            
        return binArr
        
    def convertToBinary(self, num):
        if num == 0:
            return '0'
        
        binaryNo = ''
        while num != 0:
            rem = num % 2
            binaryNo = str(rem) + binaryNo
            num = num // 2
        return binaryNo
        
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        binaryArr = []
        totalHD = 0
        for i in nums:
            binaryNum = self.convertToBinary(i)
            binaryArr.append(binaryNum)
        
        longest_string = max(binaryArr, key=len)
        maxLenInArr = len(longest_string)
        modifiedBinaryArr = self.modifyBinArr(maxLenInArr, binaryArr)
        for j in range(len(modifiedBinaryArr)):
            for k in range(1, len(modifiedBinaryArr)):
                if j >= k:
                    continue
                totalHD += self.findHammingDistance(modifiedBinaryArr[j], modifiedBinaryArr[k])
        
        
        return totalHD
        

mySolution = Solution()
nums = [6,1,8,6,8]
ans = mySolution.totalHammingDistance(nums)
print("#####", ans)