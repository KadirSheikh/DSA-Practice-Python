class Solution(object):
    def binarySearchLastOccurance(self, arr, x):
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
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return index
        
mySol = Solution()

sample_array = [1, 2, 3, 4, 5, 5, 5, 6]
x = 5

LBS = mySol.binarySearchLastOccurance(sample_array, x)
print(LBS+1)
