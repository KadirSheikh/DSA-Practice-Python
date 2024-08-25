class Solution(object):
    
    def calculateScope(self, pointOne, pointTwo):
        x1 = pointOne[0]
        y1 = pointOne[1]
        
        x2 = pointTwo[0]
        y2 = pointTwo[1]

        if x1 - x2 == 0:
            return ''
        
        slope = (y2 - y1) / float(x2 - x1)
        
        return slope
    
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        self.coordinates = coordinates
        
        if len(coordinates) <= 2:
            return True
            
        firstPoint = coordinates[0]
        
        slopesArr = []
            
        for secondPoint in coordinates[1:len(coordinates)]:
            slope = self.calculateScope(firstPoint, secondPoint)
            slopesArr.append(slope)
            
        return len(set(slopesArr)) == 1