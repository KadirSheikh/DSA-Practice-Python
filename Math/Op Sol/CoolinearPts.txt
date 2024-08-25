class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        self.coordinates = coordinates
        
        pointOne = coordinates[0]
        pointTwo = coordinates[1]
        
        x1 = pointOne[0]
        y1 = pointOne[1]
        
        x2 = pointTwo[0]
        y2 = pointTwo[1]
        
        xMove = x2 - x1
        yMove = y2 - y1
        
        
        for i in range(1, len(coordinates)):
            firstPt = coordinates[i-1]
            secondPt = coordinates[i]
            
            x = secondPt[0] - firstPt[0]
            y = secondPt[1] - firstPt[1]
            
            if y * xMove != x * yMove:
                return False
                
        return True