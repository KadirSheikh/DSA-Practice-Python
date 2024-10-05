class Solution(object):
    def findMaxRecursion(self, arr, low):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.low = low
        
        if low == len(arr) - 1:
            return arr[low]
        temp = self.findMaxRecursion(arr, low + 1)
        return max(arr[low], temp)

        
mySol = Solution()
sample_array = [0, 1, 2, 3, 13, 51, 6, 7, 8, 9]
low = 0
ans = mySol.findMaxRecursion(sample_array, low)
print("ans", ans)