class Solution(object):
    def binarySearchFirstOccurance(self, arr, x):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.x = x
        
        low = 0
        high = len(arr) - 1
        index = -1
        arr.sort()
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                index = mid
                high = mid - 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return index
        
mySol = Solution()

sample_array = [0, 1, 2, 5, 6, 8, 9, 9, 9, 10, 11, 18]
x = 9

FBS = mySol.binarySearchFirstOccurance(sample_array, x)
print(FBS+1)