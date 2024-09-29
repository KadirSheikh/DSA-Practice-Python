class Solution(object):
    def findAllOccurrences(self, arr, x):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.x = x
        
        lowFirst = 0
        highFirst = len(arr) - 1
        
        lowLast = 0
        highLast = len(arr) - 1
        
        
        firstOcc = -1
        lastOcc = -1
        
        arrAllOcc = []
        arr.sort()
        
        while lowFirst <= highFirst:
            midFirst = (lowFirst + highFirst) // 2
            
            if arr[midFirst] == x:
                firstOcc = midFirst
                highFirst = midFirst - 1
            elif arr[midFirst] > x:
                highFirst = midFirst - 1
            else:
                lowFirst = midFirst + 1
                
                
        while lowLast <= highLast:
            midLast = (lowLast + highLast) // 2
            
            if arr[midLast] == x:
                lastOcc = midLast
                lowLast = midLast + 1
            elif arr[midLast] > x:
                highLast = midLast - 1
            else:
                lowLast = midLast + 1
                
        if firstOcc != -1 and lastOcc != -1:
            for i in range(firstOcc, lastOcc + 1):
                arrAllOcc.append(i)
        
        return arrAllOcc
        
mySol = Solution()

sample_array = [0, 1, 2, 5, 6, 8, 9, 9, 9, 9, 10, 11, 18]
x = 9

FBS = mySol.findAllOccurrences(sample_array, x)
print(FBS)