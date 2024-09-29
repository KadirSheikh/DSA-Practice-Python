class Solution(object):
    def lastOccuranceLS(self, arr, x):
        """
        :type date: str
        :rtype: int
        """
        
        self.arr = arr
        self.x = x
        lastOccured = -1
        for i in range(0, len(arr)):
            if arr[i] == x:
                lastOccured = i
                
        return lastOccured
                
mySol = Solution()

arr = [2, -1, 5, 10, -20, 30, -20, 10, 10, 30, 50]
x = 10

lastOccLS = mySol.lastOccuranceLS(arr, x)
print(lastOccLS)
