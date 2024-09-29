class Solution(object):
    def linerSearch(self, arr, x):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.x = x
        
        for i in arr:
            if arr[i] == x:
                return i
        return -1
                
mySol = Solution()

sample_array = [4, 7, 2, 9, 1, 5, 3, 8, 6, 0]
x = 9

LS = mySol.linerSearch(sample_array, x)
print(LS)