class Solution(object):
    def checkPrimePostion(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] == 2 and i in [2,3,5,7]:
                count += 1
            if arr[i] != 1 and arr[i] % 2 == 1 and i in [2,3,5,7]:
              count += 1
              
        return count
        
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        
        numArr = []
        count = 0
        for i in range(1, n+1):
            numArr.append(i)
        
        for i in numArr:
            first = numArr[0]
            numArr = numArr[1:len(numArr)]
            numArr.append(first)
            count += self.checkPrimePostion(numArr)
        
        return count

mySol = Solution()

n = 5
numberOfArr = mySol.numPrimeArrangements(n)
print(numberOfArr)