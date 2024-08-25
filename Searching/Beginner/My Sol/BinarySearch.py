class Solution(object):
    def binarySearch(self, arr, x):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.x = x
        
        low = 0
        high = len(arr)
        arr.sort()
        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
mySol = Solution()

sample_array = [0, 1, 2, 3, 13, 5, 6, 7, 8, 9]
x = 13

BS = mySol.binarySearch(sample_array, x)
print(BS)