class Solution(object):
    def binarySearchRecursion(self, arr, low, high, x):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.low = low
        self.high = high
        self.x = x
        
        mid = (low + high) // 2
        
        # Base case: if low index is greater than high, x is not found
        if low > high:
            return -1
            
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
            return self.binarySearchRecursion(arr, low, high, x)
        else:
            low = mid + 1
            return self.binarySearchRecursion(arr, low, high, x)

        
mySol = Solution()

sample_array = [0, 1, 2, 3, 13, 5, 6, 7, 8, 9]
sample_array.sort()
x = 13
low = 0
high = len(sample_array) - 1
BS = mySol.binarySearchRecursion(sample_array, low, high, x)
print(BS)