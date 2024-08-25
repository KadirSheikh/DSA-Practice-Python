class Solution(object):
    
    def findNegBS(self, arr):
        self.arr = arr
        
        count = -1
        low = 0
        high = len(arr) - 1
 
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < 0:
                count = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return count
        
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        count = 0
        
        if len(grid) == 0:
            return count
            
        for i in grid:
            occ = self.findNegBS(i)
            if occ != -1:
                count = count + (len(i) - occ)
            
        return count
        