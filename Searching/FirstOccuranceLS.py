class Solution(object):
    def firstOccuranceLS(self, arr, x):
        """
        :type date: str
        :rtype: int
        """
        
        self.arr = arr
        self.x = x
        
        for i in range(0, len(arr)):
            if arr[i] == x:
                return i
        return -1
                
mySol = Solution()

arr = [2, -1, 5, 10, -20, 30, -20, 10, 10, 30, 50]
x = 10
fistOccLS = mySol.firstOccuranceLS(arr, x)
print(fistOccLS)
