class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
        self.date = date
        
        dateOfArray = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        date = int(date.split('-')[2])
        
        totalDays = date
        
        for i in range(month - 1):
            totalDays += dateOfArray[i]
        
        if month > 2 and year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            totalDays+= 1
            
        return totalDays

mySol = Solution()

dayOfYr = mySol.dayOfYear("2012-01-02")

print(dayOfYr)