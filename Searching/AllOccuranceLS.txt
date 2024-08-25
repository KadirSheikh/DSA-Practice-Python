class Solution(object):
    def allOccurances(self, arr, x):
        """
        :type date: str
        :rtype: int
        """
        
        self.arr = arr
        self.x = x
        allOccurance = []
        for i in range(0, len(arr)):
            if arr[i] == x:
                allOccurance.append(i)
                
        return allOccurance  
mySol = Solution()

arr = [2, -1, 5, 10, -20, 30, -20, 10, 10, 30, 50]
x = 10
allOccuLS = mySol.allOccurances(arr, x)
print(allOccuLS)