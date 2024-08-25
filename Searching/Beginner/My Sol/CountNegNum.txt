class Solution(object):
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
            for j in i:
                if j < 0:
                    count += 1
            
        return count